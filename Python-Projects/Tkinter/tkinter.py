


import tkinter
from tkinter import * #what widgets do we want to import, we can just say all:*


#Frame is the parent class within tkinter
#A frame is a rectangular region on the screen.
#It is used to organize a group of widgets

    #the self keyword passes in elements of a class into functions.
    #Every element in a Python program is an object of a class.

    #define the first function: def __init__(self, master):
    #so now we can reference our class as self
    #and our Frame as master
    #P is going to first run this function with the __init__ if it's there
    #The __init__ method lets the class initialize the object's attributes
    #The python __init__ method is declared within a class and
    #is used to initialize the attributes of an object as soon as the object
    #is formed. The default parameter, named 'self' is always passed in its argument.
    #This self represents the object of the class itself.


#this is so we have the blueprints to create a tkinter window:
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        #use self to reference class items
        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter')
        self.master.config(bg="lightgrey")

        #add widgets to it: how to write and paint things on the screen:
        #check what are the variable classes for tkinter, like StringVar(), BooleanVar(), IntVar(), DoubleVar()


        self.varFName = StringVar()
        self.varLName = StringVar()

        #self.varFName.set('Bob') we could assign it like this
        #self.varLName.set('Smith')
        #print(self.varFName.get()) and then print it on the screen like this
        #print(self.varLName.get())

        #now we are going to paint to our textbox:
        #we are calling one of tkinter's widgets = Entry: one line textbox for user input
        #self.master is telling it where to place that input
        #pack() is the paint command = to paint it / or have it appear on the tkinter screen
        
        #referenced website: https://ttamanagement.github.io/

        self.lblFName = Label(self.master, text="First Name: ", font=('Helvetica', 16), fg="black", bg="lightgrey")
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.lblLName = Label(self.master, text="Last Name: ", font=('Helvetica', 16), fg="black", bg="lightgrey")
        self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master, text="", font=('Helvetica', 16), fg="black", bg="lightgrey")
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        self.txtFName = Entry(self.master,text=self.varFName, font=('Helvetica', 16), fg="black", bg="lightblue")
        self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        self.txtLName = Entry(self.master,text=self.varLName, font=('Helvetica', 16), fg="black", bg="lightblue")
        self.txtLName.grid(row=1, column=1, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit", font=('Helvetica', 16), command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", font=('Helvetica', 16), command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)


    #self is the class, submit is the method
        #store the inputs in the variables: like the fn
        #get is the built in method to get and store
        #config = use it to change something dynamically in the middle of when it's running, inside: text will equal to a new value
    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))

        #the command to close the window is destroy() and self.master is the name of the window
    def cancel(self):
        self.master.destroy()

if __name__ == "__main__":
    #instantiation = calling on the class = we are calling on Tkinter
    #instantiated the class with Tk(), then we need to pass it into something = root
    root = Tk()
    App = ParentWindow(root) #we attached root into ParentWindow
    root.mainloop() #this is how we can make it continuously function, keep it alive
