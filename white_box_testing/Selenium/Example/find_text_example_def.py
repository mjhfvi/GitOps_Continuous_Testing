''' TBD'''
from __future__ import annotations

from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

now = datetime.now()
current_time = now.strftime('%H:%M:%S')
print('\n============================================\nSelenium Starting Tests at: ', current_time,
      '\n============================================\n')

chrome_options = Options()
chrome_service = Service('C:/repository/SeleniumExamples/chromedriver.exe')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
chrome_options.add_argument('--remote-debugging-pipe')
chrome_options.add_argument('--headless=new')  # disable starting browser
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-extensions')  # disabling extensions
chrome_options.add_argument('--disable-gpu')  # applicable to windows os only
chrome_options.add_argument('--disable-default-apps')
chrome_options.add_argument('--no-default-browser-check')
chrome_options.add_argument('--start-maximized')
# chrome_options.add_argument("--ignore-certificate-errors")
# chrome_options.add_argument("--profile-directory=Default")
# chrome_options.add_argument("--user-data-dir=C:/Temp/ChromeProfile")
chrome_options.page_load_strategy = 'normal'

# Setup chrome driver
chrome_driver = webdriver.Chrome(
    options=chrome_options, service=chrome_service)
# chrome_driver.refresh()
chrome_driver.minimize_window()

chrome_driver.get('https://www.google.com/')

# Get page title
chrome_title = chrome_driver.title

# Test if title is correct
# print('Printing the Title Information:', title, '\n')

# Example for finding text
# SEARCH_TEXT = "Google"

# if SEARCH_TEXT in chrome_title:
#     print(f'The Title Element Contains the Text: {SEARCH_TEXT}\nTEST 01: `title` Test Passed\n')
# else:
#     print(f'The Title Element does not Contain the Search Text: {SEARCH_TEXT}',
#           '\nTEST 01: `title` Test did NOT Passed\n')


# def search_text(text):
#     ''' Example for Finding Text in Defined Function '''
#     search_for_text = text
#     if search_for_text in chrome_title:
#         print(f'The Title Element Contains the Text: {search_for_text}',
#               '\nTEST 02: `title` Test Passed\n')
#     else:
#         print(f'The Title Element does not Contain the Search Text: {search_for_text}',
#               '\nTEST 02: `title` Test did NOT Passed\n')


def search_text(text_information='text', element_name='element not defined', test_number='00'):
    ''' Example for Finding Text in Defined Function '''
    search_for_text = text_information
    set_test_number = test_number

    try:
        if search_for_text in chrome_title:
            print(f'The {element_name} Element Contains the Text: {search_for_text}',
                  f'\nTEST {set_test_number}: `{element_name}` Test Passed\n')
        else:
            print(f'The {element_name} Element does not Contain the Search Text: {search_for_text}',
                  f'\nTEST {set_test_number}: `{element_name}` Test did NOT Passed\n')
    except NameError:
        print('Variable x is not defined')


search_text(text_information='Google', element_name='Title', test_number='01')

# Find the search field element by its ID
element = chrome_driver.find_element(By.NAME, 'q')

# Input text into the search field
element.clear()
element.send_keys('test')
element.send_keys(Keys.RETURN)

page_source = chrome_driver.page_source
# print('Printing Page Source: ', page_source, '\n')

# test if the page source contains the search text
search_text(text_information='Google',
            element_name='Page Source', test_number='02')

# Close the driver
print('\n\n============================================\nSelenium Tests Are Done at: ',
      current_time, '\nExiting....\n============================================\n')
sleep(2)
chrome_driver.close()
