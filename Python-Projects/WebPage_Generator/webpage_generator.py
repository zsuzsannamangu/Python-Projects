
#
# Python:   3.11.5
#
# Author:   Zsuzsanna Mangu
#
# Purpose:  This is a program that can open an HTML file in Chrome
#           and diplay the user input on that page
#


import tkinter as tk
from tkinter import *
import webbrowser
import os

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(600, 300))

        self.varInput = StringVar()

        self.lblInput = Label(self.master, text="Your text: ", font=('Helvetica', 16), fg="black")
        self.lblInput.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        # call the Entry widget to get input from the user
        self.txtInput = Entry(self.master,text=self.varInput, font=('Helvetica', 16), fg="black")
        self.txtInput.grid(row=0, column=1, columnspan=3, padx=(10,10), pady=(30,0), sticky=W+E)

        self.btnDefault = Button(self.master, text="DefaultHTML", font=('Helvetica', 16), command=self.defaultHTML)
        self.btnDefault.grid(row=2, column=0, padx=(90,10), pady=(30,0), sticky=NE)

        self.btnSubmit = Button(self.master, text="CustomHTML", font=('Helvetica', 16), command=self.customHTML)
        self.btnSubmit.grid(row=2, column=1, padx=(10,10), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", font=('Helvetica', 16), command=self.cancel)
        self.btnCancel.grid(row=2, column=2, padx=(10,10), pady=(30,0), sticky=NE)


    def defaultHTML(self):
        htmlText = "Stay tuned"
        # to open/create a new html file in the write mode:
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body><h1>" + htmlText + "</h1>\n</body></html>"
        # writing the code into the file:
        htmlFile.write(htmlContent)
        # close the file:
        htmlFile.close()
        # open html file in Chrome:
        # call html file using open_new_tab()
        filename = 'file:///'+os.getcwd()+'/' + 'index.html'
        webbrowser.open_new_tab(filename)
        
    def customHTML(self):       
        # get() is a built in method to get user input, we store it in a variable:
        htmlText = self.varInput.get()
        # to open/create a new html file in the write mode:
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body><h1>" + htmlText + "</h1>\n</body></html>"
        # writing the code into the file:
        htmlFile.write(htmlContent)
        # close the file:
        htmlFile.close()
        # open html file in Chrome:
        # call html file using open_new_tab()
        filename = 'file:///'+os.getcwd()+'/' + 'index.html'
        webbrowser.open_new_tab(filename)

    # add a function here to close the window using the destroy() method
    def cancel(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()






