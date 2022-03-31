
from tkinter import *

#creating a window and assigning it the varaible "win"
win = Tk()
f = Frame(win)

#create buttons
b1 = Button(f, text="One")
b2 = Button(f, text = "Two")
b3 = Button(f, text = "Three")
#b4 = Button(win, text = "Four")
b1.configure(text = "uno")
#place buttons using "pack" method. This packs button into parent (window)
#Default is TOP

b1.pack(side = LEFT)
b2.pack(side = LEFT)
b3.pack(side = LEFT)
#b4.pack(side = BOTTOM)

l = Label(win, text ="this is a label over buttons")

l.pack()
f.pack()

def but1():
    print("Button one was pushed")

b1.configure(command = but1) #this is called "call back" as the function
# is an argument of the configure function. 



win.mainloop()


