from __future__ import annotations

import logging
import sys

import coloredlogs
import requests
# import time

format = '%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s'
logger = logging.getLogger('Api_Requests_Log')
coloredlogs.install(level='DEBUG', logger=logger, fmt=format)  # DEBUG, INFO, WARNING, ERROR, CRITICAL


def test_api(WEBSITE_URL):
    try:
        response = requests.get(WEBSITE_URL, timeout=10)  # , verify=False
        # print(response)
        # print(SITE_URL)
        # print(response.status_code)

        if response.status_code == 200:
            logger.info('API Request Call is Successful')
            test_status = 'Pass'
            return test_status
        else:
            logger.error('API Request Call is Unsuccessful, Killing Run')
            exit()
    except Exception as ERROR:
        logger.error('An Unexpected error occurred,', ERROR)


if __name__ == '__main__':
    # help(sys.modules['__main__'])
    logger.info('End of File')
    sys.exit()
