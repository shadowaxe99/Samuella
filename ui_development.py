"""This module is responsible for UI development."""

from tkinter import *


def create_window():
    window = Tk()
    window.title('AI Assistant')
    window.geometry('350x200')
    lbl = Label(window, text='Hello')
    lbl.grid(column=0, row=0)
    btn = Button(window, text='Click Me')
    btn.grid(column=1, row=0)
    window.mainloop()