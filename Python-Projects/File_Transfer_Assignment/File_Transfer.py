
#
# Python:   3.11.5
#
# Author:   Zsuzsanna Mangu
#
# Purpose:  This is a program that can move files from one folder
#           to another with a click of a button.
#

import tkinter as tk
from tkinter import *

import tkinter.filedialog

#we import the shutil module that is used to transfer files
import os
import shutil

import time
import datetime
from datetime import timedelta

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #Sets title of GUI Window:
        self.master.title("File Transfer")

        #Creates button to select files from source directory:
        #The sourceDir(self) function asks the user to pick a directory, see the function below
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #Positions source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))


        #Creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #Positions destination button in GUI using tkinter grid()
        #on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15,10))

        #Creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0,15))

        #Creates an Exit button
        self.exit_btn = Button(text="Exit", width=10, command=self.exit_program)
        #Positions the Exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    #Creates function to select source directory:
    #The sourceDir function will ask the user to pick the directory to insert into the source Entry widget
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #The .delete(0, END) will clear the content that is inserted in the Entry widget,
        #this allows the path to be inserted into the Entry widget properly.
        self.source_dir.delete(0, END)
        #The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)

        
    #Creates a function to select destination directory:
    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, selectDestDir)

    #Creates function to transfer files from one directory to another
    def transferFiles(self):
        #Gets source directory
        source = self.source_dir.get()
        #Gets destination directory
        destination = self.destination_dir.get()
        #Gets a list of files in the source directory
        source_files = os.listdir(source)
        #Runs through each file in the source directory
        
        for i in source_files:

            #get the timestamp of the file:
            path = os.path.join(source, i)

            #get the time of last modification of the path with the getmtime() function
            #the return value is a floating point number giving the number of seconds since the epoch (Jan 1, 1970, 00:00:00 UTC)
            modification_time = os.path.getmtime(path)

            #A timedelta object represents a duration, the difference between two dates or times
            #Here we use hours=24, but it can be minutes = ..., days=... etc.

            #we substract 24 hours from the current date+time
            hours_24 = datetime.datetime.now() - timedelta(hours = 24)

            """time = datetime.datetime.now()
            returns this format: 2023-10-23 13:43:26.007725

            timedelta = timedelta(hours=24)
            returns this format: 1 day, 0:00:00

            hours_24 = datetime.datetime.now() - timedelta(hours = 24)
            returns this format: 2023-10-22 13:43:26.442720"""

            #we convert the timestamp we got into a date object with the fromtimestamp() function
            date_time_file = datetime.datetime.fromtimestamp(modification_time)

            #if the difference in hours is less than 24 hours, move the file(s):
            if hours_24 < date_time_file:
                #moves each file from the source to the destination:
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred.')
            else:
                print("There are no new files here!")

    #Creates function to exit program
    def exit_program(self):
        #root is the main GUI window, the Tkinter destroy method
        #tells Python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()






                
