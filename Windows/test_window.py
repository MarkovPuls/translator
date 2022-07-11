import requests
import json
import tkinter
from tkinter import *

window = Tk()
window.geometry(f"240x300+700+300")
window.config(bg='#6be97e')
window.title('Калькулятор')


m = tkinter.Entry(window, justify=tkinter.LEFT, font=('Arial', 15), width=15)
m.grid(row=0, column=0, columnspan=4, sticky='we', padx=5)


def text():
    a = m.get()
    return a


but1 = tkinter.Button(window, text="Перевод", bd=5, font=('Arial', 14), fg='red', command=lambda: text())
but1.grid(row=1, column=0, columnspan=4, sticky='we', padx=5)

world = tkinter.Label(window, text=a, font=('Arial', 15), width=15)
world.grid(row=3, column=0, columnspan=4, sticky='we', padx=5)


window.grid_columnconfigure(0, minsize=60)
window.grid_rowconfigure(0, minsize=60)
window.mainloop()
