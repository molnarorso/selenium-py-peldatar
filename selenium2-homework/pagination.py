from selenium import webdriver
import csv

PATH = "C:\\Users\\ors\\Downloads\\chromedriver.exe"
URL = "http://localhost:9999/pagination.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)
browser.implicitly_wait(2)

header1 = browser.find_element_by_xpath("//th[normalize-space()='Id']").text
header2 = browser.find_element_by_xpath("//th[normalize-space()='First name']").text
header3 = browser.find_element_by_xpath("//th[normalize-space()='Second name']").text
header4 = browser.find_element_by_xpath("//th[normalize-space()='Surname']").text
header5 = browser.find_element_by_xpath("//th[normalize-space()='Second Surname']").text
header6 = browser.find_element_by_xpath("//th[normalize-space()='Birth date']").text
my_field_names = [header1, header2, header3, header4, header5, header6]

with open('csvpaginationhoz.csv', 'w') as my_file1:
    my_reader1 = csv.DictWriter(my_file1, my_field_names)
    my_reader1.writeheader()


def my_function(range_beginning, range_end):
    for i in range(range_beginning, range_end):
        id_number = browser.find_element_by_xpath(f"/html/body/div/div/div/table/tbody/tr[{i}]/td[1]").text
        first_name = browser.find_element_by_xpath(f"/html/body/div/div/div/table/tbody/tr[{i}]/td[2]").text
        second_name = browser.find_element_by_xpath(f"/html/body/div/div/div/table/tbody/tr[{i}]/td[3]").text
        surname = browser.find_element_by_xpath(f"/html/body/div/div/div/table/tbody/tr[{i}]/td[4]").text
        second_surname = browser.find_element_by_xpath(f"/html/body/div/div/div/table/tbody/tr[{i}]/td[5]").text
        birth_date = browser.find_element_by_xpath(f"/html/body/div/div/div/table/tbody/tr[{i}]/td[6]").text
        if first_name.startswith('A'):
            with open('csvpaginationhoz.csv', 'a') as my_file2:
                my_reader2 = csv.DictWriter(my_file2, my_field_names)
                my_reader2.writerow({
                    header1: id_number,
                    header2: first_name,
                    header3: second_name,
                    header4: surname,
                    header5: second_surname,
                    header6: birth_date})




my_function(1, 11)
browser.find_element_by_xpath("//button[normalize-space()='»']").click()
my_function(1, 11)
browser.find_element_by_xpath("//button[normalize-space()='»']").click()
my_function(1, 5)


browser.quit()
