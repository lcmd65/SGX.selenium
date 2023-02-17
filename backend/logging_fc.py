import logging
from backend.string_define import type_of_data
from backend.string_define import file_handler_url
from backend.date_fc import *
class log_data:
    def __init__ (self, time_dl, file_dl):
        self.time_dl = time_dl
        self.file_dl = file_dl

list_logging = []

def logging_fc(file_name_input):
    log_format = '%(asctime)s -' +file_name_input+'- %(message)s'
    logger = logging.getLogger(__name__)
    logger.setLevel('DEBUG')
    formatter = logging.Formatter(log_format)
    file_handler = logging.FileHandler(file_handler_url)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.info("action from project")

def logging_fc_traceback(file_name_log,curent_date_time, file_dload):
    with open(file_name_log,'r') as f:
        for line in f:
            if curent_date_time in line:
                if file_dload in line:
                    return True
        return False

def check_all_logging_fc(curent_date_time,file_name_log):
    for i in range(4):
        for item in type_of_data:
            if logging_fc_traceback(file_name_log, string_date(curent_date_time), item) == False:
                list_logging.append(log_data(curent_date_time,))
        curent_date_time = make_last_day(curent_date_time)
    return list_logging
