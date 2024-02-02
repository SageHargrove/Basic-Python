from tkinter import *


class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.p1 = Label(master, text="Try to", fg="black", bg="cyan")
        self.p1.pack(side=LEFT, fill=Y, expand=0)

        self.p2 = Label(master, text = "Recreate this", fg="white", bg="magenta")
        self.p2.pack(side=TOP, fill=Y, expand=1)

        self.p3 = Label(master, text="in Python", fg="white", bg="orange")
        self.p3.pack(side=LEFT, fill=X)

window = Tk()
app = App(window)
window.mainloop()