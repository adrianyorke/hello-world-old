#!/usr/bin/env python
"""Module docstring [pylint-C0111]."""

import logging

# INFO: https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
#ch = logging.StreamHandler()
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
handler.setFormatter(formatter)

# add ch to logger
logger.addHandler(handler)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
