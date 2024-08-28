#author: puneetsd
import os
import logging


def get_logger(name):
    log_level = os.environ['LOG_LEVEL']
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    return logger

def handler(event, context):
    logger = get_logger(__name__)
    logger.info("Hello")
    logger.info(event)
    logger.info(context)
    
