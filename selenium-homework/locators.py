from selenium import webdriver

PATH = "C:\\Users\\ors\\Downloads\\chromedriver.exe"
URL = "http://localhost:9999/kitchensink.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

try:
    element1 = browser.find_element_by_id("openwindow")
    element2 = browser.find_element_by_name("courses")
    element3 = browser.find_element_by_xpath('//*[@id="name"]')
    print(element1.text)
    print(element2.tag_name)
    print(element3.get_attribute("class"))
except:
    print("An error occurred")