''' TBD '''
from __future__ import annotations

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTest01():
    def __init__(self):
        print('Starting')
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_test01(self, text='Dictionary'):
        self.driver.get('https://www.google.com/')
        self.driver.find_element(By.ID, 'APjFqb').send_keys(text)
        self.driver.find_element(By.ID, 'APjFqb').send_keys(Keys.ENTER)
        # element.send_keys(Keys.ENTER)
        # self.driver.find_element(By.CSS_SELECTOR, ".gJBeNe").click()
        # assert self.driver.find_element(By.CSS_SELECTOR, ".gJBeNe").text == "Dictionary"


TestTest01().test_test01(text='test')
