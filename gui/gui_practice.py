import tkinter as tk
from tkinter import Button, Label
import os
import os.path as osp
import natsort as nt

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master= master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = Button(self, text="QUIT", fg="red",
                              command=self.quit)
        self.quit.pack(side="bottom")

        self.calculate = Button(self)
        self.calculate["text"] = "Get file list"
        self.calculate["command"] = self.get_filelist
        self.calculate.pack(side="right")

    def say_hi(self):
        print("hi there, everyone!")

    def calc(self):
        a = 1
        b = 3
        print(f"a + b = {a+b}")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
