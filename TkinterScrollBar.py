from tkinter import *

win = Tk() #getting access to all Tk module

#LESSON: how to get info from text input, and how to set text to window:

#v = StringVar() #setting the variable v to stringVar method () which
#holds a string variable.
#v.set("this is set by the program")
#e = Entry(win, textvariable = v) #entry method accepts single line text
#strings from a user. 
#e.pack()#positions the entry window using pack geometry manager. 

#LESSON:how to make a list box and scroll bar:

lb = Listbox(win, height = 6)
lb.pack() #use pack method to place the list box
lb.insert(END,"first entry") #syntax: insert(position,string)
lb.insert(END,"second entry")
lb.insert(END,"third entry")
lb.insert(END,"fourth entry")

sb = Scrollbar(win, orient=VERTICAL)
sb.pack(side = LEFT, fill = Y) #fill − Determines whether widget fills any
#extra space allocated to it by the packer, or keeps its own minimal
#dimensions: fill = Y means fill only vertically.

#Insert elements in to the listbox

for values in range(100):
    lb.insert(END, values)

#attaching lb to sb. Since we have vertical sc use "yscrollcommand.
# the "set" command sets sb to listbox
lb.configure(yscrollcommand=sb.set)
# configuring the scroll box to have a vertical view on the list box 
sb.configure(command=lb.yview)


if __name__ == "__main__":

    win.mainloop()

    
