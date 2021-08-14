from selenium import webdriver
import csv
import pyautogui

PATH = "C:\\Users\\ors\\Downloads\\chromedriver.exe"
URL = "http://localhost:9999/another_form.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()

browser.get(URL)
browser.implicitly_wait(2)
with open('table_in.csv', 'r', newline='', encoding='utf-8') as my_source_file:
    my_reader = csv.DictReader(my_source_file)
    for i in my_reader:
        browser.implicitly_wait(1)
        browser.find_element_by_xpath("//input[@id='fullname']").clear()
        browser.find_element_by_xpath("//input[@id='fullname']").send_keys(i['Name'])
        browser.find_element_by_xpath("//input[@id='email']").clear()
        browser.find_element_by_xpath("//input[@id='email']").send_keys(i['Email'])

        date_of_birth = i['DoB']
        new_form_of_dob = date_of_birth.split('-')
        pyautogui.press('tab')
        pyautogui.write(new_form_of_dob[2])
        pyautogui.write(new_form_of_dob[1])
        pyautogui.write(new_form_of_dob[0])

        browser.find_element_by_xpath("//input[@id='phone']").clear()
        browser.find_element_by_xpath("//input[@id='phone']").send_keys(i['Phone'])
        browser.find_element_by_xpath("//input[@id='submit']").click()
        browser.implicitly_wait(1)

browser.implicitly_wait(1)
browser.find_element_by_xpath("//button[normalize-space()='Export HTML table to CSV file']").click()
