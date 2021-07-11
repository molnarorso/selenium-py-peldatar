from selenium import webdriver

PATH = "C:\\Users\\ors\\Downloads\\chromedriver.exe"
URL = "http://localhost:9999/minesweeper-game.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)
flag = True
boxes_to_click = browser.find_elements_by_class_name('covered')
for boxes in boxes_to_click:
    boxes.click()





