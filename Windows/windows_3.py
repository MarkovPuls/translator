import tkinter
from tkinter import *
from  tkinter import ttk

# Ввод текстовой информации Entry

window = Tk()
window.geometry(f"500x300+700+300")


def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('Не заполненое сообщение')


def get_del():
    name.delete(0, 'end')
    name2.delete(0, 'end')


def get_pas():
    print(name.get())
    print(name2.get())


tkinter.Label(window, text='Введите текст').grid(row=0, column=0)
tkinter.Label(window, text='Введите пароль').grid(row=1, column=0)

name = tkinter.Entry(window)
name.grid(row=0, column=1)

name2 = tkinter.Entry(window, show=')')
name2.grid(row=1, column=1)

tkinter.Button(window, text='Нажимай', command=get_entry).grid(row=2, column=0, sticky='w')
tkinter.Button(window, text='Удалить', command=get_del).grid(row=2, column=1, sticky='w')
tkinter.Button(window, text='<--------', command=lambda: name.insert(0, 'Ну, Здарова отец')) \
    .grid(row=0, column=2, sticky='w')
tkinter.Button(window, text='Показать', command=get_pas).grid(row=1, column=2, sticky='w')

tkinter.Checkbutton(window, text='Как дела?').grid(row=3, column=0, sticky='w')
tkinter.Checkbutton(window, text='Как дела?', indicatoron=0).grid(row=4, column=0, sticky='w')


def select_g():
    g = d.get()
    k.set(f"Выбор {g}")
    if g == 1:
        print('Easy')
    elif g == 2:
        print('Normal')
    elif g == 3:
        print('Hard')


d = tkinter.IntVar()
k = tkinter.StringVar()

tkinter.Radiobutton(window, text='Как дела?', variable=d, value=1, command=select_g).grid(row=5, column=0, sticky='w')
tkinter.Radiobutton(window, text='Как дела?', variable=d, value=2, command=select_g).grid(row=6, column=0, sticky='w')
tkinter.Radiobutton(window, text='Как дела?', variable=d, value=3, command=select_g).grid(row=7, column=0, sticky='w')
tkinter.Label(window, textvariable=k).grid(row=8, column=0, sticky='w')

Kek = ("qwe", 'asd', 'zxc')

ttt = ttk.Combobox(window, values=Kek)
ttt.current(1)
ttt.grid(row=9, column=0, sticky='w')

window.grid_columnconfigure(0, minsize=100)
window.grid_columnconfigure(1, minsize=100)
window.grid_columnconfigure(2, minsize=100)
window.mainloop()
