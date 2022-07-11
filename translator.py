import requests
import json

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'ZTBlZDhiMWItOWQ2OS00OGYxLWE5NzktZWJkYjAyZGNkYjcyOmZlNWE3MzI0MWM2ZDRkMjNhOGUzYWQwYjJhNjU3NzNl'
headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)
print(auth.text)

if auth.status_code == 200:
    token = auth.text

    while True:
        word = input('Введи слово: ')
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
            except ValueError:
                print('Слово не найдено')
        elif word == 'end':
            exit()

else:
    print('Ошибка. Что-то пошло не так...')
