''' chrome driver folder, TBD '''
# Chromium Command Line Switches: https://peter.sh/experiments/chromium-command-line-switches/
# Emulation: https://chromedevtools.github.io/devtools-protocol/tot/Emulation/
from __future__ import annotations

import logging
import sys

import coloredlogs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

format = '%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s'
logger = logging.getLogger('Driver_Settings_Log')
coloredlogs.install(level='DEBUG', logger=logger, fmt=format)  # DEBUG, INFO, WARNING, ERROR, CRITICAL

# Chrome Driver Geolocation
coordinates = {
    'latitude': 50.1109,
    'longitude': 8.6821,
    'accuracy': 100
}
# --------------- imports   --------------- #

# CHROME_PATH = 'C:/repository/SeleniumExamples/chromedriver.exe'
CHROME_PATH = 'C:/repository/SeleniumExamples/myProject/tools/chromedriver.exe'
USER_DATA_DIR = 'C:/Temp/SeleniumChromeProfile'
# --------------- constants --------------- #


def _driver() -> object:
    ''' Help chrome_driver Module: no arg yet, TBD ...'''
    logger.info('Building Settings for Chrome Drive')
    try:
        # print(f"{Color.BLUE}{'DEBUG:'}{Color.OFF} Building Chrome Driver: {Color.BLUE}{__name__}{Color.OFF}")
        # From Selenium Import Webdriver
        chrome_options = Options()
        chrome_service = Service(CHROME_PATH)
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # chrome_options.add_argument('--disable-dev-shm-usage')  # disable shared memory, for Linux
        # chrome_options.add_argument('--remote-debugging-pipe=chrome_pipe')  #  debug Chrome remotely
        # chrome_options.add_argument('--remote-debugging-port=9222')  #  debug Chrome remotely
        chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
        chrome_options.add_argument('--disable-gpu')  # applicable to windows os only
        chrome_options.add_argument('--no-default-browser-check')  # disable the default browser check on startup
        # bypass certificate errors to HTTPS or self-signed cert
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--allow-insecure-localhost')
        chrome_options.add_argument('--disable-extensions')  # disabling extensions
        chrome_options.add_argument('--disable-plugins')
        chrome_options.add_argument('--disable-translate')
        chrome_options.add_argument('--disable-default-apps')  # disable the default apps that are bundled with Chrome
        # specify the directory where user profiles are stored
        chrome_options.add_argument('--profile-directory=Default')
        chrome_options.add_argument('--lang=en-US')  # Set Browser Language, en-US
        # chrome_options.add_argument('--default-country-code=America/Los_Angeles')
        # chrome_options.add_argument('--user-data-dir=C:\\Temp\\SeleniumChromeProfile')
        # chrome_options.add_argument('--profile-directory=Profile 1')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--deny-permission-prompts')
        chrome_options.add_argument('--debug-print')
        # chrome_options.add_argument('--headless')  # Disable Starting Browser
        chrome_options.page_load_strategy = 'none'  # normal(default), eager, none(Does not block WebDriver at all)
        logger.info('Starting Chrome Driver to Work')

        # ==== Initialize Selenium Web Driver ==== #
        chrome_driver = webdriver.Chrome(options=chrome_options,
                                         service=chrome_service,
                                         keep_alive=False)
        chrome_driver.refresh()
        chrome_driver.minimize_window()
        chrome_driver.implicitly_wait(10)
        # chrome_driver.execute_cdp_cmd("Emulation.setGeolocationOverride", coordinates)

        return chrome_driver
    except Exception as ERROR:
        logger.error('An Unexpected error occurred,', ERROR)


if __name__ == '__main__':
    try:
        _driver()
        help(sys.modules['__main__'])
        logger.info('End of File')
        logging.shutdown()
        sys.exit()
    except Exception as ERROR:
        logger.error('An Unexpected error occurred', ERROR)
    # finally:

if __name__ != '__main__':
    try:
        logger.info('Run Started From Main Script')
    except Exception as ERROR:
        logger.error('An Unexpected error occurred', ERROR)
    # finally:
