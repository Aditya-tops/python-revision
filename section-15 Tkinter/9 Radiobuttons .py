from tkinter import *

def selected():
    label.config(text="Choice of fuel is : " + fuel.get())

root = Tk()
root.geometry("300x300")

fuel = StringVar(value='Diesel')

redio1 = Radiobutton(root, text="Petrol", variable=fuel, value="Petrol", command=selected)
redio2 = Radiobutton(root, text="Diesel", variable=fuel, value="Diesel", command=selected)
redio3 = Radiobutton(root, text="Electric", variable=fuel, value="Electric", command=selected)

redio1.pack()
redio2.pack()
redio3.pack()

label = Label(root)
label.pack()

root.mainloop()