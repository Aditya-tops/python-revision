from tkinter import *

def project_click():
    print("Project menu item clicked")

root = Tk()
mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)

mymenu.add_cascade(label='File', menu=submenu)

submenu.add_command(label='Project', command=project_click)
submenu.add_command(label='Save', command=project_click)

status = Label(root, text="This is the current status", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

toolbar = Frame(root, bg='green')
insertbutton = Button(toolbar, text="Insert Files", command=project_click)
deletebutton = Button(toolbar, text="Delete Files", command=project_click)

insertbutton.pack(side=LEFT, padx=2, pady=3)
deletebutton.pack(side=LEFT, padx=2, pady=3)

toolbar.pack()  # Add this line to add the toolbar to the root window

root.mainloop()