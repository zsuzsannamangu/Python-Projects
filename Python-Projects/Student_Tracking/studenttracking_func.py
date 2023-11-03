#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.11.5
#
# Author:       Zsuzsanna Mangu
#
# Purpose:      This is a Student Tracking System Application, using Python with
#               Tkinter and SQLite3.
#
# Tested OS:    This code was written and tested to work with Mac OS Ventura 14.0

import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

import studenttracking_main
import studenttracking_gui


def center_window(self, w, h):
    #Tkinter components adjust the window size according to user-defined geometry.
    #In order to get the screen size, we can use winfo_screenwidth() & winfo_screenheight()
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    # .geometry() sets the geometry/dimensions of the frame
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
    #close the app:
        self.master.destroy()
        os._exit(0)
    
def create_db(self):
    conn=sqlite3.connect('db_studenttracking.db')
    with conn: #if we have connection:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_studenttracking( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_currentcourse TEXT \
            );")
        conn.commit()
    conn.close()
    first_run(self)
            

def first_run(self):
    conn = sqlite3.connect('db_studenttracking.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_studenttracking (col_fname,col_lname,col_fullname,col_phone,col_email,col_currentcourse) VALUES (?,?,?,?,?,?)""", ('John','Doe','John Doe','111-111-1111','jdoe@email.com', 'math'))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("SELECT COUNT(*) FROM tbl_studenttracking")
    #fetchone() will extract the very first one
    #fetchone() retrieves the next row of a query result set and returns a single sequence, or None if no more rows are available. 
    count = cur.fetchone() [0]
    return cur,count

#this is referring to the event listener in the studenttracking_gui file, when the user selects from our list
#select item in ListBox:

def onSelect(self,event):
    #calling the event is the self.lstList1 widget, whatever is triggering the event
    varList = event.widget
    #curselection() returns a tuple containing the line NUMBERS of the selected element or elements, counting from 0. If nothing is selected, returns an empty tuple.
    select = varList.curselection() [0]
    #get() returns a tuple containing the TEXT of the lines with indices from first to last, inclusive.
    value = varList.get(select)
    conn = sqlite3.connect('db_studenttracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT col_fname,col_lname,col_phone,col_email,col_currentcourse FROM tbl_studenttracking WHERE col_fullname = (?)", [value])
        varBody = cursor.fetchall()
        #This returns a tuple and we can slice it into 4 parts using data[] during the iteration
        #delete (first, last=None): Deletes the lines whose indices are in the range [first, last]. If the second argument is omitted, the single line with index first is deleted.
        #insert(index,*elements): inserts one or more new lines into the listbox before the line specified by index. Use END as the first argument if you want to add new lines to the end of the listbox.
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_currentcourse.delete(0,END)
            self.txt_currentcourse.insert(0,data[4])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    #normalize the data to keep it consistent in the database
    var_fname = var_fname.strip() #this will remove any blank spaces before and after the user's entry
    var_lname = var_lname.strip()
    var_fname = var_fname.title() #this will ensure that the first character in each word is capitalized
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname))
    print("var_fullname: {}".format(var_fullname))

    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_currentcourse = self.txt_currentcourse.get().strip()

    if not "@" or not "." in var_email: #will use this soon
          print("Incorrect email format")
          #if any of these are empty we are giving an error msg to the user, bc they didn't fill out the fields
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_currentcourse) > 0):
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cursor = conn.cursor()
            # Check the database for existance of the fullname, if so we will alert user and disregard request
            cursor.execute("SELECT COUNT(col_fullname) FROM tbl_studenttracking WHERE col_fullname = '{}'".format(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: # if this is 0 then there is no existence of the fullname and we can add new data
                print("chkName: {}".format(chkName))
                cursor.execute("INSERT INTO tbl_studenttracking (col_fname,col_lname,col_fullname,col_phone,col_email,col_currentcourse) VALUES (?,?,?,?,?,?)",(var_fname,var_lname,var_fullname,var_phone,var_email,var_currentcourse))
                self.lstList1.insert(END, var_fullname) # update listbox with the new fullname
                onClear(self) # call the function to clear all of the textboxes
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                onClear(self) # call the function to clear all of the textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.")

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) # Listbox's selected value
    conn = sqlite3.connect('db_studenttracking.db')
    with conn:
        cur = conn.cursor()
        # check count to ensure that this is not the last record in
        # the database...cannot delete last record or we will get an error
        cur.execute("SELECT COUNT(*) FROM tbl_studenttracking")
        count = cur.fetchone()[0]
        if count > 1:
            #The askokcancel() function shows a confirmation dialog that has two buttons: OK and Cancel.
            #syntax: answer = askokcancel(title, message, **options)
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permenantly deleted from the database. \n\nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('db_studenttracking.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM tbl_studenttracking WHERE col_fullname = '{}'".format(var_select))
                onDeleted(self) # call the function to clear all of the textboxes and the selected index of listbox
######             onRefresh(self) # update the listbox of the changes
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select,var_select))
    conn.close()

def onDeleted(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_currentcourse.delete(0,END)
##    onRefresh(self) # update the listbox of the changes
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_currentcourse.delete(0,END)
    

def onRefresh(self):
    # Populate the listbox, coinciding with the database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('db_studenttracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM tbl_studenttracking")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
                cursor.execute("SELECT col_fullname FROM tbl_studenttracking")
                varList = cursor.fetchall()[i]
                for item in varList:
                    self.lstList1.insert(0,str(item))
                    i = i + 1
    conn.close()

def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0] # index of the list selection
        var_value = self.lstList1.get(var_select) # list selection's text value
    except:
        #showinfo() is a built in information message box in tkinter
        #syntax: tkinter.messagebox.showinfo(title=None, message=None, **options)
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Update request.")
        return
    # The user will only be alowed to update changes for phone, emails and currentcourse.
    # For name changes, the user will need to delete the entire record and start over.
    var_phone = self.txt_phone.get().strip() # normalize the data to maintain database integrity
    var_email = self.txt_email.get().strip()
    var_currentcourse = self.txt_currentcourse.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_currentcourse > 0)): # ensure that there is data present
        conn = sqlite3.connect('db_studenttracker.db')
        with conn:
            cur = conn.cursor()
            # count records to see if the user's changes are already in
            # the database...meaning, there are no changes to update.
            cur.execute("SELECT COUNT(col_phone) FROM tbl_studenttracking WHERE col_phone = '{}'".format(var_phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("SELECT COUNT(col_email) FROM tbl_studenttracking WHERE col_email = '{}'".format(var_email))
            count2 = cur.fetchone()[0]
            print(count2)
            cur.execute("SELECT COUNT(col_currentcourse) FROM tbl_studenttracking WHERE col_currentcourse = '{}'".format(var_currentcourse))
            count3 = cur.fetchone()[0]
            print(count3)
                                                          
            if count == 0 or count2 == 0 or count3 == 0: # if proposed changes are not already in the database, then proceed
                response = messagebox.askokcancel("Update Request","The following changes ({}) and ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_phone,var_email,var_currentcourse,var_value))
                print(response)
                if response:
                    #conn = sqlite3.connect('db_studenttracking.db')
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("UPDATE tbl_studenttracking SET col_phone = '{0}',col_email = '{1}',col_currentcourse = '{2}' WHERE col_fullname = '{3}'""".format(var_phone,var_email,var_currentcourse,var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request","No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected","Both ({}) and ({}) \nalready exist in the database for this name. \n\nYour update request has been cancelled.".format(var_phone, var_email, var_currentcourse))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information","Please select a name from the list. \nThen edit the phone or email information.")
    onClear(self)


if __name__ == "__main__":
    pass






                                  
            











        
