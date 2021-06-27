from selenium import webdriver

PATH = "C:\\Users\\ors\\Downloads\\chromedriver.exe"

URL = "https://manna.hu"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)


