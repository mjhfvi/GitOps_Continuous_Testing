'''this is the core folder, TBD'''
# https://docs.python.org/3/library/logging.html#logging-levels
from __future__ import annotations

import logging

import coloredlogs

format = '%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s'
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger, fmt=format)  # DEBUG, INFO, WARNING, ERROR, CRITICAL


logger.info(f"Initializing {__name__} Packages ...")
