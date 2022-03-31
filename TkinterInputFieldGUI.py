from tkinter import *

root = Tk()

label1 = Label(root, text="Name")
entry1 = Entry(root)

label2 = Label(root, text="Email Address")
entry2 = Entry(root)

label1.grid(row = 0, column = 0, sticky = W)
entry1.grid(row = 0, column = 1)
label2.grid(row = 1, column = 0)
entry2.grid(row = 1, column = 1)

root.mainloop()
