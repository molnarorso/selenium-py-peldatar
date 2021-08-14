from selenium import webdriver

PATH = "C:\\Users\\ors\\Downloads\\chromedriver.exe"
URL = "http://localhost:9999"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

elements = browser.find_elements_by_tag_name('a')
links = []

for i in elements:
    links.append(i.get_attribute('href'))

with open('linkekhezfajl.txt', 'w') as f:
    for j in links:
        f.write(j + '\n')

print(len(links))
