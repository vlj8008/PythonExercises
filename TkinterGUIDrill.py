import tkinter as tk
from tkinter import *


class mainwindow (Frame): #mainwindow is child class of Frame class
    def __init__(self, master):#master is keyword which references "Frame"

        
        self.master = master
        self.master.resizable(width = True, height = True)
        self.master.geometry('590x200')
        self.master.title("Check Files")
        self.master.config(bg='lightgray')

        self.btn_top = Button(self.master, width=20, height=2, text="Browse...")
        self.btn_top.grid(row=0,column=0,pady=(40,0),padx=5)

        self.txt_box_top = Entry(self.master, text="", width=60)
        self.txt_box_top.grid(row=0,column=1, pady=(40,0), columnspan=5, ipady=6)

        self.btn_mid = Button(self.master, width=20, height=2, text="Browse...")
        self.btn_mid.grid(row=1,column=0,pady=(5,0),padx=1)

        self.btn_bot_left = Button(self.master, width=20, height=3, text="Check for files...")
        self.btn_bot_left.grid(row=2,column=0,pady=5, padx=5)

        self.btn_bot_right = Button(self.master, width=20, height=3, text="Close Program")
        self.btn_bot_right.grid(row=2,column=5,pady=5, padx=5, columnspan=5)

        self.txt_box2 = Entry(self.master, text="", width=60)
        self.txt_box2.grid(row=1,column=1, pady=(5,0), columnspan=5, ipady=6)

if __name__ == "__main__":
        root = Tk() # classes usually start with capital letter. Here we instantiate tkinter and assign it "root"
        App = mainwindow(root)
        root.mainloop() #makes window stay alive. 





    
