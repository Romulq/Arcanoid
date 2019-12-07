from tkinter import *


class Window:
    def __init__(self):
        self.window = Tk()
        self.window.title("Правила игры")
        self.window.geometry('644x344')

        self.image = PhotoImage(file="img/rule.png")
        self.lbl = Label(self.window, image=self.image).place(x=0, y=0)

        self.window.mainloop()
