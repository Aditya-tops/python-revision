from tkinter import *

def selected():
    lable.config(text=check_value.get())

root = Tk() 
root.geometry("300x300")

check_value = BooleanVar()
checkbutton = Checkbutton(root,text="Accept terms",variable=check_value,command=selected)
checkbutton.pack()

lable = Label(root)
lable.pack()

root.mainloop() 