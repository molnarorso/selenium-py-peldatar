import time

from selenium import webdriver
import pyautogui
import pyperclip

PATH = "C:\\Users\\ors\\Downloads\\chromedriver.exe"
URL = "http://localhost:9999/editable-table.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()

browser.get(URL)
browser.implicitly_wait(2)


def tabbing():
    pyautogui.press('tab')


def completing_entry(my_data):
    pyautogui.write(my_data)


browser.find_element_by_xpath("//button[normalize-space()='Add']").click()
browser.implicitly_wait(2)
browser.find_element_by_xpath("//tbody/tr[7]/td[1]/input[1]").send_keys('Goat cheese')
tabbing()
completing_entry('12.99')
tabbing()
completing_entry('30')
tabbing()
completing_entry('Dairy')

browser.find_element_by_xpath("//button[normalize-space()='Add']").click()
browser.implicitly_wait(2)
browser.find_element_by_xpath("//tbody/tr[8]/td[1]/input[1]").send_keys('Carrots')
tabbing()
completing_entry('1.99')
tabbing()
completing_entry('1000')
tabbing()
completing_entry('Vegetables')

time.sleep(0.5)
browser.find_element_by_xpath("//input[@placeholder='Search...']").click()
pyautogui.write('ba')
time.sleep(0.5)
search_results1 = browser.find_elements_by_class_name("eachRow")
assert len(search_results1) == 3
pyautogui.write('s')
search_results2 = browser.find_elements_by_class_name("eachRow")
assert len(search_results2) == 2

time.sleep(1)
browser.quit()




