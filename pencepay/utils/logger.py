import logging
import os


def get_logger(name=__name__):
    current_folder = os.path.dirname(__file__)
    log_file = '{path}/logs.log'.format(path=current_folder)

    logger = logging.getLogger(name)
    handler = logging.FileHandler(filename=log_file)
    formatter = logging.Formatter('%(module)s: %(asctime)s | %(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    return logger
