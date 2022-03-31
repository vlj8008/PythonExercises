
import tkinter
from tkinter import * #astericks means import all. 

class ParentWindow(Frame): #"frame" is parent class within tkinter, so we are inheriting what tkinter has. The frame is like a container 
    def __init__ (self, master): #references class as "self", and Frame as master
        Frame.__init__(self) #Below defines the class, and root = Tk() instantiates these attributs below:

        self.master = master #this is primary window that will pop up on screen
        self.master.resizable(width = True, height = True ) #allows user to resize the screen
        self.master.geometry('{}x{}'.format(700,400)) # geometry method determines dimensions of window
        self.master.title('Learning Tkinter')
        self.master.config(bg='lightgray')

        self.varFName = StringVar() #StringVar means "variable will be holding the string.
        self.varLName = StringVar()
        '''
        self.varFName.set('Bob') "set" assigns a value to the var FName.
        self.varLName.set('Smith')

        print(self.varFName.get()) "get" gets the value
        print(self.varLName.get())

        '''

        self.lblFName = Label(self.master, text = 'First Name: ', font = ("Helvetica", 16),fg='black', bg = 'lightgray')#instantiating a label widget
        self.lblFName.grid(row = 0, column = 0, padx = (30, 0), pady= (30,0)) #grid is a placement manager, meaning it places widgets using a grid layout. 

        self.lblLName = Label(self.master, text = 'Last Name: ', font = ("Helvetica", 16),fg='black', bg = 'lightgray')
        self.lblLName.grid(row = 1, column = 0, padx = (30, 0), pady= (30,0))

        self.lblDisplay = Label(self.master, text = '', font = ("Helvetica", 16),fg='black', bg = 'lightgray')
        self.lblDisplay.grid(row = 3, column= 1, padx = (0, 0), pady= (30,0), sticky = NE)

        self.txtFName = Entry(self.master, text=self.varFName, font = ("Helvetica", 16),fg='black', bg = 'lightblue')#entry method creates a small one line entry box where user can enter.
#Open and closed bracktets calls that class "Entry". "Self.master" means place text box on main window. Then give text the variable Fname. 

        self.txtFName.grid(row= 0, column=1, padx = (30, 0), pady= (30,0)) #painting text box on to the main window at position row 0, and column 1.

        self.txtLName = Entry(self.master, text=self.varLName, font = ("Helvetica", 16),fg='black', bg = 'lightblue')
        self.txtLName.grid(row = 1, column= 1, padx = (30, 0), pady= (30,0))

        self.btnSubmit = Button(self.master, text = "Submit", width = 10, height = 2, command=self.submit) #"command" means what command will be invoked. self = class, submit means method. 
        self.btnSubmit.grid(row = 2, column= 1, padx = (0, 0), pady= (30,0), sticky = NE)

        self.btnCancel = Button(self.master, text = "Cancel", width = 10, height = 2, command = self.cancel)
        self.btnCancel.grid(row = 2, column= 1, padx = (0, 90), pady= (30,0), sticky = NE) #sticky means "where do we want it to stick. 

    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text = 'Hello {} {} !'.format(fn,ln)) #config makes something change dynamically while program is running.


    def cancel(self):
        self.master.destroy()







if __name__ == "__main__":
        root = Tk() # classes usually start with capital letter. Here we instantiate tkinter and assign it "root"
        App = ParentWindow(root)
        root.mainloop() #makes window stay alive. 
