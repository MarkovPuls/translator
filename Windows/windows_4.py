import tkinter
from tkinter import *
from tkinter import messagebox

# Калькулятор питониста и пиониста

window = Tk()
window.geometry(f"240x300+700+300")
window.config(bg='#6be97e')
window.title('Калькулятор')

m = tkinter.Entry(window, justify=tkinter.RIGHT, font=('Arial', 15), width=15)   # Поле ввода
m.insert(0, '0')
m.grid(row=0, column=0, columnspan=4, sticky='we', padx=5)


def add_g(get):
    value = m.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    m.delete(0, 'end')
    m.insert(0, value + get)


def add_ope(ope):
    value = m.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calcu()
        value = m.get()
    m.delete(0, 'end')
    m.insert(0, value + ope)


def press_key(event):
    print(event.char)
    if event.char.isdigit():
        add_g(event.char)
    elif event.char in '+-*/':
        add_ope(event.char)
    elif event.char in '\r':
        calcu()


def clear():
    m.delete(0, 'end')
    m.insert(0, 0)


def make_but(n):
    return tkinter.Button(text=n, bd=5, font=('Arial', 14), command=lambda: add_g(n))


def make_op(ope):
    return tkinter.Button(text=ope, bd=5, font=('Arial', 14), fg='red', command=lambda: add_ope(ope))


def calcu():
    value = m.get()
    if value[-1] in '-+/*':
        value = value + value[:-1]
    m.delete(0, 'end')
    try:
        m.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание', 'Написал хуйню, давай все по новой')
        m.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'На ноль делить нелья')
        m.insert(0, 0)


def make_call(c):
    return tkinter.Button(text=c, bd=5, font=('Arial', 14), fg='blue', command=calcu)


def make_clear(c):
    return tkinter.Button(text=c, bd=5, font=('Arial', 14), fg='blue', command=clear)


window.bind('<Key>', press_key)

make_but('1').grid(row=1, column=0, sticky='wens', pady=5, padx=5)
make_but('2').grid(row=1, column=1, sticky='wens', pady=5, padx=5)
make_but('3').grid(row=1, column=2, sticky='wens', pady=5, padx=5)
make_but('4').grid(row=2, column=0, sticky='wens', pady=5, padx=5)
make_but('5').grid(row=2, column=1, sticky='wens', pady=5, padx=5)
make_but('6').grid(row=2, column=2, sticky='wens', pady=5, padx=5)
make_but('7').grid(row=3, column=0, sticky='wens', pady=5, padx=5)
make_but('8').grid(row=3, column=1, sticky='wens', pady=5, padx=5)
make_but('9').grid(row=3, column=2, sticky='wens', pady=5, padx=5)
make_but('0').grid(row=4, column=0, sticky='wens', pady=5, padx=5)

make_op('+').grid(row=1, column=3, sticky='wens', pady=5, padx=5)
make_op('-').grid(row=2, column=3, sticky='wens', pady=5, padx=5)
make_op('/').grid(row=3, column=3, sticky='wens', pady=5, padx=5)
make_op('*').grid(row=4, column=3, sticky='wens', pady=5, padx=5)

make_call('=').grid(row=4, column=2, sticky='wens', pady=5, padx=5)
make_clear(')(').grid(row=4, column=1, sticky='wens', pady=5, padx=5)

window.grid_columnconfigure(0, minsize=60)
window.grid_columnconfigure(1, minsize=60)
window.grid_columnconfigure(2, minsize=60)
window.grid_columnconfigure(3, minsize=60)

window.grid_rowconfigure(0, minsize=60)
window.grid_rowconfigure(1, minsize=60)
window.grid_rowconfigure(2, minsize=60)

window.mainloop()
