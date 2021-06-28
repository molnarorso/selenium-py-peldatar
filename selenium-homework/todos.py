from selenium import webdriver

PATH = "C:\\Users\\ors\\Downloads\\chromedriver.exe"
URL = "http://localhost:9999/todo.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

e = browser.find_elements_by_class_name("done-false")


