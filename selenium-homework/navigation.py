from selenium import webdriver

PATH = "C:\\Users\\ors\\Downloads\\chromedriver.exe"
URL = "http://localhost:9999/general.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

elements = browser.find_elements_by_tag_name('a')

for element in elements:

    browser.implicitly_wait(10)
    element.click()
    browser.implicitly_wait(10)

    try:
        browser.switch_to.window(browser.window_handles[1])
        browser.implicitly_wait(10)
        x = browser.current_url
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
    except:
        x = browser.current_url

        # try:
        #     alert_pop = browser.switch_to.alert
        #     browser.implicitly_wait(10)
        #     alert_pop.accept()
        #     browser.implicitly_wait(10)
        #     # browser.back()
        # except:
        #     pass

    if x == element.get_attribute('href'):
        print('Okay')


    else:
        print("Not okay")
        browser.back()

