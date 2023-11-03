#!/usr/bin/python
"""
    #!/usr/bin/python
    It's a recommended way, proposed in documentation:
    2.2.2. Executable Python Scripts.
    In a Unix-like operating system, the program loader
    takes the presence of these two characters as an
    indication that the file is a script, and tries to
    execute that script using the interpreter specified
    by the rest of the first line in the file.
"""
# -*- coding: utf-8 -*-
"""
    # -*- coding: utf-8 -*-
    This sets the charset if it is present on the first two lines of the file.
    this is Syntax to declare the encoding of a Python source file. It's discussed
    in PEP 0263 - Defining Python Source Code Encodings.
    https://www.python.org/dev/peps/pep-0263/
"""
#
# Python Ver:   3.11.5
#
# Author:       Zsuzsanna Mangu
#
# Purpose:      This is a Student Tracking System Application, using Python with
#               Tkinter and SQLite3.
#
# Tested OS:    This code was written and tested to work with macOS Ventura 14.0

from tkinter import *
import tkinter as tk
from tkinter import messagebox

# Be sure to import our other modules 
# so we can have access to them
import studenttracking_gui
import studenttracking_func

# Frame = the Tkinter frame class is the class that our own class will inherit from
# Frame = the primary Tkinter object
# master = the name of the frame, the first frame of Tkinter = Frame
# self = it's like the address to get to the ParentWindow class = ParentWindow
# self.master = the ParentWindow Frame


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        
        #define the master frame configuration:
        self.master = master
        self.master.minsize(500,300) #this is how big the window will be that holds our form
        self.master.maxsize(500,300) #min and max size locks the window, so it can't be resized by user

        #we refer to the studenttracking_func file and call its center_window function
        studenttracking_func.center_window(self,500,300) #w=500, h=300
        self.master.title("Student Tracking")
        self.master.configure(bg="lightgrey")

        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: studenttracking_func.ask_quit(self))
        arg = self.master

        #load in the GUI widgets
        studenttracking_gui.load_gui(self)

        #initiate the Tkinter menu dropdown object
        #this menu will appear on the top of our window
        
        #The goal of this widget = Menu() is to allow us to create menus that
        #can be used by our applications.
        #The core functionality provides ways to create three menu types:
        #pop-up, toplevel and pull-down.
        #syntax : w = Menu(master, option, ...)
        #master is the parent window
        #options can be used as key-value pairs separated by commas, ex: (master, bg, Font, Image...etc)
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff = 0)
        
        #tearoff menu = a menu that can be made into a window and moved to another portion of the screen
        #setting tearoff = 0: the menu will not have a tear-off feature
        filemenu.add_separator()


        
        #add_separator(): Adds a separator line to the menu.
        filemenu.add_command(label="Exit", underline=1, accelerator="Ctrl+Q",command=lambda: studenttracking_func.ask_quit(self))
        
        #add_command(options): Adds a menu item to the menu.
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        
        #add_cascade(options): Creates a new hierarchical menu by associating a given menu to a parent menu.
        
        helpmenu = Menu(menubar, tearoff = 0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        
        helpmenu.add_separator()
        
        helpmenu.add_command(label="How to use this program")
        
        helpmenu.add_separator()
        
        helpmenu.add_command(label="About")# add_command is a child menubar item of the add_cascade parent item

        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)

        
        #Finally, we apply the config method of the widget to display the menu:
        #we could pass in additional aprams for additional functionality or appearances such as a borderwidth.

        self.master.config(menu=menubar, borderwidth='1')

        
#The (if __name__ == "__main__":) part is basically telling Python that if this script
#is ran, it should start by running the code below this line....in this case we have
#instructed Python to run the following and in this order:

#root = tk.TK() : This instantiates the Tk.() root frame (window) into being
#App = ParentWindow(root): This instantiates our own class as an App object
#root.mainloop() : it will stay open until we instruct it to close

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
        












        

        

        





        

        
        
