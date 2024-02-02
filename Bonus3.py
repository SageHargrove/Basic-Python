from tkinter import *


class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.p1 = Label(master, text="Try to", fg="black", bg="cyan")
        self.p1.grid(row=0, column=0, sticky = NE)

        self.p2 = Label(master, text = "Recreate this", fg="white", bg="magenta")
        self.p2.grid(row=1, column=0)

        self.p3 = Label(master, text="in Python", fg="white", bg="orange")
        self.p3.grid(row=1, column=1)

window = Tk()
app = App(window)
window.mainloop()