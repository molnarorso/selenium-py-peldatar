from selenium import webdriver
import time

PATH = "C:\\Users\\ors\\Downloads\\chromedriver.exe"
URL = "http://localhost:9999/windowgame.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

browser.implicitly_wait(2)
target_color = browser.find_element_by_xpath("//p[@id='target_color']").text

for i in range(0, 100):
    button_xpath = f"//button[@id='{i}']"
    browser.find_element_by_xpath(button_xpath).click()
    browser.switch_to.window(browser.window_handles[1])
    color_code_from_other_window = browser.find_element_by_xpath("/html/body/h1").text
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    browser.implicitly_wait(0.2)
    if target_color != color_code_from_other_window:
        continue
    else:
        print('Match')
        break

browser.quit()
