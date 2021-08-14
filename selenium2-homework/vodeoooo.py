import time

from selenium import webdriver
from selenium.webdriver import ActionChains
import pyautogui

PATH = "C:\\Users\\ors\\Downloads\\chromedriver.exe"
URL = "http://localhost:9999/videos.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)
browser.implicitly_wait(5)

# TC01: Playing first video
browser.find_element_by_xpath("//video[@id='html5video']").click()
time.sleep(4)

# TC02: Stopping first video
browser.find_element_by_xpath("//video[@id='html5video']").click()

# TC03: Playing second video
browser.find_element_by_xpath("//button[normalize-space()='Play/Pause']").click()
time.sleep(4)

# TC04: Stopping second video
browser.find_element_by_xpath("//button[normalize-space()='Play/Pause']").click()

# TC05: Playing third video
browser.find_element_by_xpath("//iframe[@id='youtubeframe']").click()
time.sleep(4)

# TC06: Playing third video
browser.find_element_by_xpath("//iframe[@id='youtubeframe']").click()

time.sleep(1)
browser.quit()

