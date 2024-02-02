from tkinter import *


class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.p1 = Label(master, text="Hello", fg="black", bg="cyan")
        self.p1.pack(side=LEFT, fill=Y, expand=1)

        self.p2 = Label(master, text = "131", fg="white", bg="magenta")
        self.p2.pack(side=LEFT, fill=X, expand=1)

        self.p3 = Label(master, text="Class", fg="white", bg="orange")
        self.p3.pack(side=RIGHT,fill=Y, expand=0)

window = Tk()
app = App(window)
window.mainloop()