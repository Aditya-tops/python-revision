from tkinter import *

root = Tk()
lable1 = Label(root,text="Email")
lable2 = Label(root,text="Password")

text1 = Entry(root)
text2 = Entry(root)

lable1.grid(row=0,column=0)
text1.grid(row=0,column=1)

lable2.grid(row=1,column=0)
text2.grid(row=1,column=1)

button = Button(root,text="LogIn")
button.grid(column=1,row=2)

root.geometry("300x300")

root.mainloop()