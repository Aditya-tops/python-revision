from tkinter import *

def selected():
    sugar = sugar_var.get()
    ice = ice_var.get()
    cream = cream_var.get()
    
    # Corrected the logic
    if sugar:
        sugar = "Sugar"
    else:
        sugar = "No Sugar"
    
    if ice:
        ice = "Ice"
    else:
        ice = "No Ice"
    
    if cream:
        cream = "Cream"
    else:
        cream = "No Cream"

    # Update label text with selected options
    label.config(text="Options selected are:\n" + sugar + "\n" + ice + "\n" + cream)

root = Tk() 
root.geometry("300x300")

# Boolean variables for checkboxes
sugar_var = BooleanVar()
ice_var = BooleanVar()
cream_var = BooleanVar()

# Corrected the variable and command references
sugar_checkbox = Checkbutton(root, text="Sugar", variable=sugar_var, command=selected)
ice_checkbox = Checkbutton(root, text="Ice", variable=ice_var, command=selected)
cream_checkbox = Checkbutton(root, text="Cream", variable=cream_var, command=selected)

# Corrected spelling for 'label'
label = Label(root)

sugar_checkbox.pack()
ice_checkbox.pack()
cream_checkbox.pack()
label.pack()

root.mainloop()
