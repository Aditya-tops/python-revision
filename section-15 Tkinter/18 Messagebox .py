from tkinter import *
import tkinter.messagebox

root = Tk()

# tkinter.messagebox.showinfo("Title","This is a messagebox")
response = tkinter.messagebox.askquestion("Question1","DO U LIKE COFFEE ?")
if response=="yes":
    print("Here is coffee for you ")


root.mainloop()