import logging
from backend.string_define import file_handler_url

def logging_fc(file_name_input):
    log_format = '%(asctime)s -' +file_name_input+'- %(message)s'
    logger = logging.getLogger(__name__)
    logger.setLevel('DEBUG')
    formatter = logging.Formatter(log_format)
    file_handler = logging.FileHandler(file_handler_url)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.info("action from project")
