import logging as l

"""
This module configures our logging options for the application.
"""

l.basicConfig(
              filename='logs/app.log',
              level=l.INFO,
              format='[%(asctime)s - %(filename)s:%(lineno)d - %(funcName)s() -%(levelname)s - %(message)s',
              datefmt='%Y-%m-%d %H:%M:%S')


def get_logger(module_name: str):
    return l.getLogger(module_name)