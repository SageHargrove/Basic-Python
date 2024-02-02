from tkinter import *

window = Tk()

listbox = Listbox(window, width=20, height=10, selectmode=SINGLE)
 
# Inserting the listbox items
listbox.insert(1, "Red")
listbox.insert(2, "Orange")
listbox.insert(3, "Yellow")
listbox.insert(4, "Green")
listbox.insert(5, "Blue")
listbox.insert(6, "Indigo")
listbox.insert(7, "Violet")
 
# Change the background color of the "Change Color" button to whatever color is currently
# selected from the listbox
def selected_item():
    for i in listbox.curselection():
        colorChanger.config(bg = listbox.get(i))

colorChanger = Button(window, text="Change Color", command=selected_item)

# Creating/packing the instruction, color options, and color changer button
instruction = Label(window, text = "Change color to:")
instruction.pack(side="top", fill=X, expand=1)

colorChanger.pack(side="right",fill=BOTH, expand=0)

listbox.pack()
 
window.mainloop()