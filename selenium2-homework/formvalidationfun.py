import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\\Users\\ors\\Downloads\\chromedriver.exe"
URL = "http://localhost:9999/simplevalidation.html"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)
time.sleep(1)

email_field = browser.find_element_by_xpath("//input[@id='test-email']")
email_validation_message = browser.find_element_by_xpath("/html/body/div/form/div[2]/div[2]")

password_field = browser.find_element_by_xpath("//input[@id='test-password']")
password_validation_message = browser.find_element_by_xpath("/html/body/div/form/div[3]/div[2]")

confirm_password_field = browser.find_element_by_xpath("//input[@id='test-confirm-password']")
confirm_password_validation_message = browser.find_element_by_xpath("/html/body/div/form/div[4]/div[2]")

customer_number_field = browser.find_element_by_xpath("//input[@id='test-customer-number']")
customer_number_validation_message = browser.find_element_by_xpath('/html/body/div/form/div[5]/div[2]')

dealer_number_field = browser.find_element_by_xpath("//input[@id='test-dealer-number']")
dealer_number_validation_message = browser.find_element_by_xpath('/html/body/div/form/div[6]/div[2]')

random_field = browser.find_element_by_xpath("//input[@id='test-random-field']")
random_field_validation_message = browser.find_element_by_xpath("/html/body/div/form/div[7]/div[2]")

date_field = browser.find_element_by_xpath("//input[@id='test-date-field']")
date_field_validation_message = browser.find_element_by_xpath("/html/body/div/form/div[8]/div[2]")

url_field = browser.find_element_by_xpath("//input[@id='test-url-field']")
url_field_validation_message = browser.find_element_by_xpath("/html/body/div/form/div[9]/div[2]")

random_textarea_field = browser.find_element_by_xpath("//textarea[@id='test-random-textarea']")
random_textarea_field_validation_message = browser.find_element_by_xpath("/html/body/div/form/div[10]/div[2]")

card_type_field = browser.find_element_by_xpath("//select[@id='test-card-type']")
card_type_field_validation_message = browser.find_element_by_xpath("/html/body/div/form/div[11]/div[2]")

card_number_field = browser.find_element_by_xpath("//input[@id='test-card-number']")
card_number_field_validation_message = browser.find_element_by_xpath("/html/body/div/form/div[12]/div[2]")

card_cvv_field = browser.find_element_by_xpath("//input[@id='test-card-cvv']")
card_cvv_field_validation_message = browser.find_element_by_xpath("/html/body/div/form/div[13]/div[2]")

expiration_month_field = browser.find_element_by_xpath("//select[@id='test-card-month']")
expiration_month_field_validation_message = browser.find_element_by_xpath("/html/body/div/form/div[14]/div[1]/div/div[2]")

expiration_year_field = browser.find_element_by_xpath("//select[@id='test-card-year']")
expiration_year_field_validation_message = browser.find_element_by_xpath("/html/body/div/form/div[14]/div[2]/div/div[2]")

single_checkbox = browser.find_element_by_xpath("//input[@id='test-single-checkbox']")
single_checkbox_validation_message = browser.find_element_by_xpath('/html/body/div/form/div[15]/div[2]')

receive_updates_checkbox_yes = browser.find_element_by_xpath("//input[@id='test-save-email-yes']")
receive_updates_checkbox_no = browser.find_element_by_xpath("//input[@id='test-save-email-no']")
receive_updates_checkbox_validation_message = browser.find_element_by_xpath("/html/body/div/form/div[16]/div[3]")

agree_terms_of_service_checkbox = browser.find_element_by_xpath("//input[@id='test-terms-service']")
agree_to_more_stuff_checkbox = browser.find_element_by_xpath("//input[@id='test-terms-service-more']")
agree_validation_message = browser.find_element_by_xpath("/html/body/div/form/div[17]/div[2]")


# TC01: Testing email field using non-complying format
email_field.clear()
email_field.send_keys('somebody@freemail.h')
time.sleep(1)
assert email_validation_message.text == 'Please check your E-Mail format'

# TC02: Testing email field by leaving it blank
email_field.clear()
email_field.send_keys('')
time.sleep(1)
assert email_validation_message.text == 'Please enter an e-mail'

# TC03: Testing email field using a complying email address that has not been registered
email_field.clear()
email_field.send_keys('somebody@freemail.hu')
time.sleep(3)
assert email_validation_message.text == 'Login does not exist'

# TC04: Testing email field using a complying email address that has been registered
email_field.clear()
email_field.send_keys('yardy@yarr.com')
time.sleep(3)
assert email_validation_message.text == ''


# TC05: Testing password field using non-complying format
password_field.clear()
password_field.send_keys('abc')
time.sleep(1)
assert password_validation_message.text == 'Should be between 6 and 20 characters'

# TC06: Testing password field using complying format
password_field.clear()
password_field.send_keys('abcdef')
time.sleep(1)
assert password_validation_message.text == ''

# TC07: Testing confirm password field using different password
confirm_password_field.clear()
confirm_password_field.send_keys('abcde')
time.sleep(1)
assert confirm_password_validation_message.text == 'Does not match Desired Password'

# TC08: Testing confirm password field by leaving it blank
confirm_password_field.clear()
confirm_password_field.send_keys('')
time.sleep(1)
assert confirm_password_validation_message.text == "This field can't be empty"

# TC09: Testing confirm password field using identical password
confirm_password_field.clear()
confirm_password_field.send_keys('abcdef')
time.sleep(1)
assert confirm_password_validation_message.text == ''

# TC10: Testing customer number field using non-complying format
customer_number_field.clear()
customer_number_field.send_keys('a')
time.sleep(1)
assert customer_number_validation_message.text == 'Should be a number'

# TC11: Testing customer number field by leaving it blank
customer_number_field.clear()
customer_number_field.send_keys('')
time.sleep(1)
assert customer_number_validation_message.text == "This field can't be empty"

# TC12: Testing customer number field using complying format
customer_number_field.clear()
customer_number_field.send_keys('8')
time.sleep(1)
assert customer_number_validation_message.text == ''

# TC13: Testing dealer number field using non-complying format
dealer_number_field.clear()
dealer_number_field.send_keys('123')
time.sleep(1)
assert dealer_number_validation_message.text == 'Should be a 4 character number'

# TC14: Testing dealer number field by leaving it blank
dealer_number_field.clear()
dealer_number_field.send_keys('')
time.sleep(1)
assert dealer_number_validation_message.text == "This field can't be empty"

# TC15: Testing dealer number field using non-complying format
dealer_number_field.clear()
dealer_number_field.send_keys('1234')
time.sleep(1)
assert dealer_number_validation_message.text == ''

# TC16: Testing random field using non-complying format
random_field.clear()
random_field.send_keys('asd')
time.sleep(1)
assert random_field_validation_message.text == 'Should contain "twelve"'

# TC17: Testing random field by leaving it blank
random_field.clear()
random_field.send_keys('')
time.sleep(1)
assert random_field_validation_message.text == ''

# TC18: Testing random field using complying format
random_field.clear()
random_field.send_keys('asdtwelve')
time.sleep(1)
assert random_field_validation_message.text == ''

# TC19: Testing date field using non-complying format
date_field.clear()
date_field.send_keys('20210814')
time.sleep(1)
assert date_field_validation_message.text == 'Must match pattern YYYY-MM-DD'

# TC20: Testing date field by leaving it blank
date_field.clear()
date_field.send_keys('')
time.sleep(1)
assert date_field_validation_message.text == "This field can't be empty"

# TC21: Testing date field using complying format
date_field.clear()
date_field.send_keys('2021-08-14')
time.sleep(1)
assert date_field_validation_message.text == ''

# TC22: Testing url field using non-complying format
url_field.clear()
url_field.send_keys('https://google.')
time.sleep(1)
assert url_field_validation_message.text == 'Please enter a valid URL (starts with "http" or "https")'

# TC23: Testing url field by leaving it blank
url_field.clear()
url_field.send_keys('')
time.sleep(1)
assert url_field_validation_message.text == ''

# TC24: Testing url field using non-complying format
url_field.clear()
url_field.send_keys('https://google.com')
time.sleep(1)
assert url_field_validation_message.text == ''

# TC25: Testing random textarea field by entering a non-complying text
random_textarea_field.clear()
random_textarea_field.send_keys('This is my text')
time.sleep(1)
assert random_textarea_field_validation_message.text == "Should be only letters and numbers"

# TC26: Testing random textarea field by leaving it blank
random_textarea_field.clear()
random_textarea_field.send_keys('')
time.sleep(1)
assert random_textarea_field_validation_message.text == "This field can't be empty"

# TC27: Testing random textarea field by entering a non-complying text
random_textarea_field.clear()
random_textarea_field.send_keys('something1')
time.sleep(1)
assert random_textarea_field_validation_message.text == ''

# TC28: Testing card type field by selecting an option
card_type_field.click()
card_type_field.send_keys(Keys.DOWN)
card_type_field.send_keys(Keys.ENTER)
time.sleep(1)
assert card_type_field_validation_message.text == ''

# TC29: Testing card type field by not selecting an option
card_type_field.click()
card_type_field.send_keys('Select Card Type')
card_type_field.send_keys(Keys.ENTER)
time.sleep(1)
assert card_type_field_validation_message.text == 'Please select a card type'

# TC30: Testing card type field by selecting another option via entering beginning of card type name
card_type_field.click()
card_type_field.send_keys('M')
card_type_field.send_keys(Keys.ENTER)
time.sleep(1)
assert card_type_field_validation_message.text == ''

# TC31 Testing card number field using non-complying number
card_number_field.clear()
card_number_field.send_keys('1234567890')
time.sleep(1)
assert card_number_field_validation_message.text == 'Please check your credit card nubmer'

# TC32: Testing card number field by leaving it blank
card_number_field.clear()
card_number_field.send_keys('')
time.sleep(1)
assert card_number_field_validation_message.text == 'Please enter a credit card number (no spaces)'

# TC33: Testing card number field using complying number
card_number_field.clear()
card_number_field.send_keys('4111111111111111')
time.sleep(1)
assert card_number_field_validation_message.text == ''

# TC34: Testing card ccv using non-complying format
card_cvv_field.clear()
card_cvv_field.send_keys('12')
time.sleep(1)
assert card_cvv_field_validation_message.text == 'Should be a number between 3 and 4 characters'

# TC35: Testing card ccv by leaving it blank
card_cvv_field.clear()
card_cvv_field.send_keys('')
time.sleep(1)
assert card_cvv_field_validation_message.text == "This field can't be empty"

# TC36: Testing card ccv using non-complying format
card_cvv_field.clear()
card_cvv_field.send_keys('123')
time.sleep(1)
assert card_cvv_field_validation_message.text == ''

# TC37: Testing expiration month field by selecting an option
expiration_month_field.click()
expiration_month_field.send_keys(Keys.PAGE_DOWN)
expiration_month_field.send_keys(Keys.ENTER)
time.sleep(1)
assert expiration_month_field_validation_message.text == ''

# TC38: Testing expiration month field by not selecting an option
expiration_month_field.click()
expiration_month_field.send_keys('Select Month')
expiration_month_field.send_keys(Keys.ENTER)
time.sleep(1)
assert expiration_month_field_validation_message.text == 'Select a month'

# TC39: Testing expiration month field by selecting an option via entering beginning of month name
expiration_month_field.click()
expiration_month_field.send_keys('F')
expiration_month_field.send_keys(Keys.ENTER)
time.sleep(1)
assert expiration_month_field_validation_message.text == ''

# TC40: Testing expiration year field by selecting an expired option via entering year
expiration_year_field.click()
expiration_year_field.send_keys('2021')
expiration_year_field.send_keys(Keys.ENTER)
time.sleep(1)
assert expiration_year_field_validation_message.text == 'Appears to be expired - please check date'

# TC41: Testing expiration year field by not selecting an option
expiration_year_field.click()
expiration_year_field.send_keys('Select Year')
expiration_year_field.send_keys(Keys.ENTER)
time.sleep(1)
assert expiration_year_field_validation_message.text == 'Select a year'

# TC42: Testing expiration year field by selecting a valid option
expiration_year_field.click()
expiration_year_field.send_keys(Keys.PAGE_DOWN)
expiration_year_field.send_keys(Keys.ENTER)
time.sleep(1)
assert expiration_year_field_validation_message.text == ''

# TC43: Testing single checkbox by selecting it
single_checkbox.click()
time.sleep(1)
assert single_checkbox_validation_message.text == ''

# TC44: Testing single checkbox by not selecting it
single_checkbox.click()
time.sleep(1)
assert single_checkbox_validation_message.text == "This field can't be empty"
single_checkbox.click() # reselecting it for submit button to work

# TC45: Testing receive updates by selecting yes
receive_updates_checkbox_yes.click()

# TC46: Testing receive updates by selecting no
receive_updates_checkbox_no.click()

# TC47: Selecting only the first option in agree to terms
agree_terms_of_service_checkbox.click()
time.sleep(1)
assert agree_validation_message.text == 'Please agree to both to continue'

# TC48: Selecting only the second option in agree to terms
agree_terms_of_service_checkbox.click()
agree_to_more_stuff_checkbox.click()
time.sleep(1)
assert agree_validation_message.text == 'Please agree to both to continue'

# TC48: Not selecting either of the options in agree to terms
agree_to_more_stuff_checkbox.click()
time.sleep(1)
assert agree_validation_message.text == 'Please agree to both to continue'

# TC48: Selecting both options in agree to terms
agree_terms_of_service_checkbox.click()
agree_to_more_stuff_checkbox.click()
time.sleep(1)
assert agree_validation_message.text == ''

submit_button = browser.find_element_by_xpath("//button[normalize-space()='Sign Up']")
submit_button.click()

browser.quit()