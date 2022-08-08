from selenium import webdriver
import chromedriver_binary
import time
from selenium.webdriver.common.by import By

bro = webdriver.Chrome()
bro.maximize_window()
bro.get('https://hd.kinopoisk.ru/')
soup = bro.find_element(By.CSS_SELECTOR, '#transactions')
soup.click()
time.sleep(5)
bro.close()


