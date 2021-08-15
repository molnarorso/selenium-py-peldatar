from selenium import webdriver
import time
from os import getcwd

PATH = "C:\\Users\\ors\\Downloads\\chromedriver.exe"
URL = "http://localhost:9999/dragndrop2.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)
time.sleep(2)

cwd = getcwd()
JS_DRAG_DROP = open(cwd + '/dnd.js', 'r').read()

cards_in_doing_column_at_first = browser.find_elements_by_xpath("//ul[@id='Doing']/li")

name_of_cards_to_move = ['Tacos', 'Pizza', 'BBQ', 'Burgers']
counter = 0
for i in name_of_cards_to_move:
    my_source = browser.find_element_by_xpath(f"//li[@id='{i}']")
    my_target = browser.find_element_by_xpath("//ul[@id='Doing']")
    browser.execute_script(JS_DRAG_DROP, my_source, my_target)
    counter += 1
    time.sleep(1)

cards_in_doing_column_after_moves = browser.find_elements_by_xpath("//ul[@id='Doing']/li")

assert len(cards_in_doing_column_after_moves) == len(cards_in_doing_column_at_first) + counter

browser.quit()