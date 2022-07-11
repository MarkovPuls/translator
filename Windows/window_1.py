import tkinter  # библиотека интерфейса
from tkinter import *

window = Tk()  # Главный цикл

photo = tkinter.PhotoImage(file='cat2.png')  # Добавление картинки
window.iconphoto(False, photo)  #  Изменение значка

window.config(bg='red')  # Фон окна
window.title('Приложение в Python')  # Название в верху

h = 500
w = 600

window.geometry(f'{h}x{w}+100+300')  # Размер окна + положение
window.resizable(False, False)  # Разрешать изменения раззмера окна
window.maxsize(700, 800)  # Максимальный и минимальный размер окна
window.minsize(300, 400)

label_1 = tkinter.Label(window, text='Hello!',  # Пишем надпись
                        bg='green',
                        fg='white',
                        font=('Arial', '25', 'bold'),
                        padx=90,  # Отступы
                        pady=10,
                        # width=4,
                        # height=7,
                        anchor='w',  # Расположение надписи
                        relief=tkinter.RAISED,  # Граници и их размер
                        bd=4,
                        justify=tkinter.RIGHT  # Выравнивание текста
                        )
label_1.pack()  # Добавляем надпись


def say_hello():  # Функция для кнопки
    print('hello')


def add_label():  # Функция для кнопки
    label_2 = tkinter.Label(window, text='New Label!')
    label_2.pack()


def counter():  # Функция счетчик при нажатии в название
    global count
    count+=1
    btn4['text'] = f'Счетчик: {count}'


count = 0  # переменная для счетчика

btn1 = tkinter.Button(window, text='Papers',  # Создание кнопки
                      command=say_hello
                      )

btn2 = tkinter.Button(window, text='New+',
                      command=add_label
                      )

btn3 = tkinter.Button(window, text='LAMBDA',
                      command=lambda: tkinter.Label(window, text='LAMBLA + TEXT').pack()  # Пишем функцию через лямбду
                      )

btn4 = tkinter.Button(window, text=f'Счетчик: {count}',
                      command=counter,
                      bg='red',
                      activebackground='blue',  # Цвет при нажатии
                      state=tkinter.DISABLED  # Блокировка кнопки!!!!
                      )

# btn1.grid(row=1, column=5, columnspan=2, sticky='we') Расположение кнопки

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()

window.mainloop()  # Что бы не закрывалось окно
