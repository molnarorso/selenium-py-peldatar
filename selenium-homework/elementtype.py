from selenium import webdriver

PATH = "C:\\Users\\ors\\Downloads\\chromedriver.exe"
URL = "http://localhost:9999/trickyelements.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

e1 = browser.find_element_by_id('randomized')
e2 = browser.find_element_by_id('difficulty')
e3 = browser.find_element_by_id('trickyForm')
e4 = browser.find_element_by_id('element1')
e5 = browser.find_element_by_id('element2')
e6 = browser.find_element_by_id('element3')
e7 = browser.find_element_by_id('element4')
e8 = browser.find_element_by_id('element5')
e9 = browser.find_element_by_id('result')

e4.click()
if e9.text == 'element1 was clicked':
    print(e9.text)
else:
    e5.click()
    if e9.text == 'element2 was clicked':
        print(e9.text)
    else:
        e6.click()
        if e9.text == 'element3 was clicked':
            print(e9.text)
        else:
            e7.click()
            if e9.text == 'element4 was clicked':
                print(e9.text)
            else:
                e8.click()
                if e9.text == 'element5 was clicked':
                    print(e9.text)