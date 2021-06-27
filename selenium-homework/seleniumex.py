from selenium import webdriver

PATH = "C:\\Users\\ors\\Downloads\\chromedriver.exe"

URL = "https://manna.hu"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

try:
    browser.find_element_by_id("nemletezik")
except:
    print("An error occurred")