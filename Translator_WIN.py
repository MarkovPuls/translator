import requests
import json
import tkinter
from tkinter import *
from tkinter import messagebox


window = Tk()
window.geometry(f"240x300+700+300")
window.config(bg='#6be97e')
window.title('Калькулятор')
m = tkinter.Entry(window, justify=tkinter.RIGHT, font=('Arial', 15), width=15)
m.grid(row=0, column=0, columnspan=4, sticky='we', padx=5)


URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'ZTBlZDhiMWItOWQ2OS00OGYxLWE5NzktZWJkYjAyZGNkYjcyOmZlNWE3MzI0MWM2ZDRkMjNhOGUzYWQwYjJhNjU3NzNl'
headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)
# print(auth.text)


def tr():
    if auth.status_code == 200:
        token = auth.text

        while True:
            # word = input('Введи слово: ')
            word = m.get()
            if word:
                headers_translate = {
                    'Authorization': 'Bearer ' + token
                }
                params = {
                    'text': word,
                    'srcLang': 1049,
                    'dstLang': 1034
                }
                r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
                res = r.json()
                try:
                    print(res['Translation']['Translation'])
                    return res
                except ValueError:
                    print('Слово не найдено')
            elif word == 'end':
                exit()
    else:
        print('Ошибка. Что-то пошло не так...')


but1 = tkinter.Button(window, text="Перевод", bd=5, font=('Arial', 14), fg='red', command=lambda: tr())
but1.grid(row=1, column=0, columnspan=4, sticky='we', padx=5)

world = tkinter.Label(window, text='res', font=('Arial', 15), width=15)
world.grid(row=3, column=0, columnspan=4, sticky='we', padx=5)

window.grid_columnconfigure(0, minsize=60)
window.grid_rowconfigure(0, minsize=60)
window.mainloop()
