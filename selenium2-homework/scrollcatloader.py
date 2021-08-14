from selenium import webdriver
import time
import shutil
import os

try:
    os.mkdir("cats2")
except FileExistsError:
    pass

PATH = "C:\\Users\\ors\\Downloads\\chromedriver.exe"
URL = "http://localhost:9999/scrolltoload.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

time.sleep(5)
for i in range(1, 11):
    text_for_file_name = browser.find_element_by_xpath(f"/html/body/div[1]/div[{i}]/p").text
    stripped_text_for_file_name = text_for_file_name.strip('Cat id: ')
    with open(f"{i}_{stripped_text_for_file_name}.png", "wb") as file:
        file.write(browser.find_element_by_xpath(f"/html/body/div[1]/div[{i}]/img").screenshot_as_png)
    shutil.move(f"{i}_{stripped_text_for_file_name}.png", 'cats2')

browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(5)
for j in range(1, 11):
    text_for_file_name = browser.find_element_by_xpath(f"/html/body/div[1]/div[{j}]/p").text
    stripped_text_for_file_name = text_for_file_name.strip('Cat id: ')
    with open(f"{j+10}_{stripped_text_for_file_name}.png", "wb") as file:
        file.write(browser.find_element_by_xpath(f"/html/body/div[1]/div[{j}]/img").screenshot_as_png)
    shutil.move(f"{j+10}_{stripped_text_for_file_name}.png", 'cats2')

browser.quit()
