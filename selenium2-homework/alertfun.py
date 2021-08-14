from selenium import webdriver
from selenium.webdriver import ActionChains
import pyautogui

PATH = "C:\\Users\\ors\\Downloads\\chromedriver.exe"
URL = "http://localhost:9999/alert_playground.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

# TC01: Testing alert button and accepting popup alert
browser.implicitly_wait(2)
browser.find_element_by_xpath("//input[@name='alert']").click()
browser.implicitly_wait(2)
alert_pop1 = browser.switch_to.alert
assert alert_pop1.text == 'I am alert'
alert_pop1.accept()

# TC02: Testing confirmation box button and accepting popup alert
browser.implicitly_wait(2)
browser.find_element_by_xpath("//input[@name='confirmation']").click()
browser.implicitly_wait(2)
alert_pop2 = browser.switch_to.alert
assert alert_pop2.text == 'I am confirm'
alert_pop2.accept()

# TC03: Testing confirmation box button and declining popup alert
browser.implicitly_wait(2)
browser.find_element_by_xpath("//input[@name='confirmation']").click()
browser.implicitly_wait(2)
alert_pop3 = browser.switch_to.alert
assert alert_pop3.text == 'I am confirm'
alert_pop3.dismiss()

# TC04: Testing prompt button and declining popup alert
browser.implicitly_wait(2)
browser.find_element_by_xpath("//input[@name='prompt']").click()
browser.implicitly_wait(2)
alert_pop4 = browser.switch_to.alert
assert alert_pop4.text == 'I am prompt'
alert_pop4.dismiss()
browser.implicitly_wait(2)
assert browser.find_element_by_xpath("//p[@id='demo']").text == ""

# TC05: Testing prompt button, entering a text, and hitting OK
browser.implicitly_wait(2)
browser.find_element_by_xpath("//input[@name='prompt']").click()
browser.implicitly_wait(2)
alert_pop5 = browser.switch_to.alert
assert alert_pop5.text == 'I am prompt'
pyautogui.write('okay')
pyautogui.press('enter')
browser.implicitly_wait(2)
assert browser.find_element_by_xpath("//p[@id='demo']").text == 'You entered: okay'

# TC06: Testing prompt button after a text has been entered before
browser.implicitly_wait(2)
browser.find_element_by_xpath("//input[@name='prompt']").click()
browser.implicitly_wait(2)
alert_pop6 = browser.switch_to.alert
assert alert_pop6.text == 'I am prompt'
pyautogui.write('')
pyautogui.press('enter')
browser.implicitly_wait(2)
assert browser.find_element_by_xpath("//p[@id='demo']").text == 'You entered:'

# TC07: Testing prompt button, entering data, but hitting Cancel
browser.get(URL)
browser.implicitly_wait(2)
browser.find_element_by_xpath("//input[@name='prompt']").click()
browser.implicitly_wait(2)
alert_pop7 = browser.switch_to.alert
assert alert_pop7.text == 'I am prompt'
pyautogui.write('okay')
alert_pop7.dismiss()
browser.implicitly_wait(2)
assert browser.find_element_by_xpath("//p[@id='demo']").text == ''

# TC08: Testing doubleclick button and accepting popup alert
browser.get(URL)
browser.implicitly_wait(2)
doubleclick_button = browser.find_element_by_id('double-click')
browser.implicitly_wait(2)
action = ActionChains(browser)
action.move_to_element(doubleclick_button)
action.double_click()
action.perform()
browser.implicitly_wait(2)
alert_pop8 = browser.switch_to.alert
assert (alert_pop8.text == 'You double clicked me!!!, You got to be kidding me')
alert_pop8.accept()
