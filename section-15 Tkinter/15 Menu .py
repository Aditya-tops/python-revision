from tkinter import *

def project_click():
    print("Project menu item clicked")

def save_click():
    print("Save menu item clicked")

root = Tk()
mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)

mymenu.add_cascade(label='File', menu=submenu)

submenu.add_command(label='Project', command=project_click)
submenu.add_command(label='Save', command=save_click)

root.mainloop()