import json
from bs4 import BeautifulSoup
import requests

# a = open('webinars.json', 'r', encoding='utf-8')
# b = json.load(a)
# var = [i['name'] for i in b]
# print(*var, sep='|')

# g = open('skillbox.html', 'r', encoding='utf-8')
# html = g.read()
# soup = BeautifulSoup(html, features="html.parser")
# links = soup.findAll('a')
# print(*[i.string.strip() for i in links], sep='\n')

pro = requests.get('https://yandex.ru/')
yat = BeautifulSoup(pro.content, features="html.parser")
water = yat.findAll(class_='direct-desktop__logo')
print(water.string.strip())






