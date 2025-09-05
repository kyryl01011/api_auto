import logging
from logging import StreamHandler, Formatter


def get_logger(logger_name: str) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    handler = StreamHandler()
    logger.addHandler(handler)

    return logger
