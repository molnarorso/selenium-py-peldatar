import time

from selenium import webdriver
import pyautogui

PATH = "C:\\Users\\ors\\Downloads\\chromedriver.exe"
URL = "http://localhost:9999/forms.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()

browser.get(URL)
browser.implicitly_wait(2)
browser.find_element_by_xpath("//input[@id='example-input-url']").click()


def tabbing():
    pyautogui.press('tab')


def completing_entry(my_data):
    pyautogui.write(my_data)


tabbing()
tabbing()
completing_entry('06')
completing_entry('05')
completing_entry('2021')

tabbing()
completing_entry('2012.05.05 05:05:05:555')

tabbing()
completing_entry('05')
completing_entry('12')
completing_entry('2000')
tabbing()
completing_entry('12')
completing_entry('01')

tabbing()
completing_entry('December')

tabbing()
completing_entry('1995')

tabbing()
completing_entry('52')
completing_entry('2015')

tabbing()
completing_entry('12')
completing_entry('25')