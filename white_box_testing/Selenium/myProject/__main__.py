''' Main Python File, TBD '''
# --------------- imports   --------------- #
from __future__ import annotations

import logging
import os
import sys
from time import perf_counter

import coloredlogs
from core import _api_requests
from core._chrome_driver_settings import _driver
from core._print_dividers import _dividers_main
from dotenv import load_dotenv
from tests import _tests01  # , _tests, _unitests
# import threading
# from concurrent.futures import as_completed
# from concurrent.futures import ThreadPoolExecutor
# from threading import Thread
# from time import sleep
# from time import time
# from altair import Element
# import time
# import threading
# from selenium.webdriver.common.by import By

format = '%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s'
logger = logging.getLogger('Main_Log')
logging.basicConfig(format=format, datefmt='%H:%M:%S', filename='main_logging.log', filemode='w')
coloredlogs.install(level='DEBUG', logger=logger, fmt=format)  # DEBUG, INFO, WARNING, ERROR, CRITICAL

# --------------- Main Function   --------------- #
SITE_URL = 'https://www.google.com/'  # 'https://www.google.com/' 'http://localhost:8080/login?from=%2F'
ELEMENT_LIST = ['.RNNXgb', '.dRYYxd']  # '.RNNXgb', '.dRYYxd', '.SDkEP'
# ELEMENT = '.RNNXgb'


def main() -> None:
    try:
        logger.info('Running Main Script Driver')
        # from selenium import webdriver
        # CHROME_DRIVER = webdriver.Chrome()  # Original Chrome Driver
        CHROME_DRIVER = _driver()  # Custom Chrome Driver
        # CHROME_DRIVER.get(SITE_URL)  # Navigate to the url

        # Get page title
        # CHROME_TITLE = CHROME_DRIVER.title
        # print('Chrome Title is:', CHROME_TITLE)

        # Find the search field element by its ID
        # CHROME_ELEMENT_NAME = 'SIvCob'  # FOR GOOGLE 'SIvCob', FOR JENKINS 'main-panel'
        # CHROME_ELEMENT = CHROME_DRIVER.find_element(By.ID, CHROME_ELEMENT_NAME)
        # CHROME_ELEMENT = CHROME_DRIVER.find_element(By.ID, CHROME_ELEMENT_NAME).text == "Google"

        # Find the search field element by its NAME
        # WEB_ELEMENT_NAME = 'q'
        # CHROME_ELEMENT = WEB_DRIVER.find_element(By.NAME, WEB_ELEMENT_NAME)

        main_script_run(CHROME_DRIVER, SITE_URL=SITE_URL)
        # main_script_run(CHROME_DRIVER=CHROME_DRIVER, CHROME_ELEMENT=CHROME_ELEMENT,
        # CHROME_ELEMENT_NAME=CHROME_ELEMENT_NAME, SITE_URL=SITE_URL)
    except Exception as ERROR:
        logger.error('An Unexpected error occurred', ERROR)


@_dividers_main
def main_script_run(CHROME_DRIVER: object, SITE_URL: str) -> None:  # CHROME_ELEMENT: object, CHROME_ELEMENT_NAME: str,
    try:
        # Start Running Tests
        # _print_dividers.main_start_dividers()
        _api_requests.test_api(SITE_URL)  # test website api

        for ELEMENT in ELEMENT_LIST:
            run_test = _tests01.SeleniumTesting(CHROME_DRIVER, SITE_URL, ELEMENT)
            run_test.find_elements_by_name()
            pass

# def run_selenium(locator):
#     driver = webdriver.Chrome()  # You can use any webdriver here
#     driver.get("https://www.google.com")  # Replace this with your URL
#     find_elements(driver, locator)
#     driver.quit()

# run_test = _tests01.SeleniumTesting(CHROME_DRIVER, SITE_URL, ELEMENT)
# locator = (By.XPATH, "//div[@class='q']")  # Example locator, modify as per your need
        # def find_elements(CHROME_DRIVER, element_id):
        #     logger.debug(f'Starting the task {element_id}...')
        #     CHROME_DRIVER.get("https://www.google.com")
        #     find_elements(CHROME_DRIVER, run_test)
            # run_test = _tests01.SeleniumTesting(CHROME_DRIVER, SITE_URL, ELEMENT)
            # run_test.find_elements_by_name()
            # sleep(1)
            # logger.debug(f'The task {element_id} completed')

        # threads = []
        # for ELEMENT in ELEMENT_LIST:
        #     thread = Thread(target=find_elements, args=(ELEMENT,))
        #     threads.append(thread)
        #     thread.start()

        # wait for the threads to complete
        # for thread in threads:
            # thread.join()

        # _print_dividers.main_end_dividers()
    except Exception as ERROR:
        logger.error('An Unexpected error occurred', ERROR)
    # finally:
        # CHROME_DRIVER.quit()  # type: ignore


if __name__ == '__main__':
    try:
        start_time = perf_counter()
        # os.system('cls')  # Clearing the screen, pre commit issue: B605:start_process_with_a_shell
        load_dotenv()  # take environment variables from .env.
        email = os.getenv('email')
        __author__ = 'Tzahi Cohen', email
        logger.debug(f'Author: {__author__}')
        main()
        # _run_test_class()
        # help(sys.modules['__main__'])
        end_time = perf_counter()
        logger.info(f'Total Run took{end_time - start_time: 0.2f} second(s) to complete.')
    except Exception as ERROR:
        logger.error('An Unexpected error occurred', ERROR)
    finally:
        print('\n' + '=' * 30 + '   End of Run   ' + '=' * 30)
        # logging.shutdown()
        sys.exit()
