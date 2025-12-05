''' define elements and find them '''
from __future__ import annotations

import logging
import sys

import coloredlogs
# import time

# coloredlogs.install()
format = '%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s'
logger = logging.getLogger('Api_Requests_Log')
coloredlogs.install(level='DEBUG', logger=logger, fmt=format)  # DEBUG, INFO, WARNING, ERROR, CRITICAL


def find_text(search_text: str, find_element: str, element_name: str):
    try:
        if search_text in find_element.text:  # type: ignore
            logger.info(f"The Element: {element_name}, Contains the Text: {search_text}.")
            run_status = 'Pass'
            return run_status
        else:
            logger.info(f"The Element: {element_name}, Does Not Contain the Text: {search_text}.")
            run_status = 'Failed'
            return run_status
    except Exception as ERROR:
        logger.error('An Unexpected error occurred,', ERROR)


def find_title(title_name: str, find_element: str):
    try:
        if title_name in find_element.text:  # type: ignore
            logger.info(f"The Title Name Contains the Text: {title_name}.")
            run_status = 'Pass'
            return run_status
        else:
            logger.info(f"The Title Name Does Not Contain the Text: {title_name}.")
            run_status = 'Failed'
            return run_status
    except Exception as ERROR:
        logger.error('An Unexpected error occurred,', ERROR)


if __name__ == '__main__':
    help(sys.modules['__main__'])
    logger.info('End of File')
    sys.exit()
