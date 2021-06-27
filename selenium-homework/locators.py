from selenium import webdriver

PATH = "C:\\Users\\ors\\Downloads\\chromedriver.exe"
URL = "http://localhost:9999/kitchensink.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

try:
    browser.find_element_by_id("openwindow")
    browser.find_element_by_name("courses")
    browser.find_element_by_xpath('//*[@id="radio-btn-example"]')
except:
    print("An error occurred")