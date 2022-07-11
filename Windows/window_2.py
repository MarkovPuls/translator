import tkinter
from tkinter import *

window = Tk()

window.geometry(f"500x300+700+300")


for m in range(5):
    for j in range(3):
        tkinter.Button(window, text=f"БАТОН").grid(row=m, column=j)  # Цикл по созданию кнопок

window.grid_columnconfigure(1, minsize=100)  # Растояние между кнопками

window.mainloop()

