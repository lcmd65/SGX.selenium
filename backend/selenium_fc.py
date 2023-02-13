from selenium import webdriver
from backend.string_define import *
from apscheduler.schedulers.blocking import BlockingScheduler
import threading
import time
from backend.logging_fc import * 

def selenium_download(): # function dload 4 file
    browser = webdriver.Chrome()
    browser.get(web_linked)
    time.sleep(10)
    temp = browser.find_element("xpath",box_linked)
    for item_temp in type_of_data:
        try:
            temp.find_element("xpath",box_element_linked).click()
            time.sleep(4)
            try:
                temp.find_element("xpath", "//*[contains(text(),'"+item_temp+"')]").click();
                logging_fc(item_temp)
            except:
                if item_temp =="Trade Cancellation Data Structure":
                    temp.find_element("xpath", "//*[contains(text(),'Trade Cancellation Data Struc...')]").click();
                    logging_fc(item_temp)
                else:
                    logging_fc("fail")
            temp.find_element("xpath",button).click()
        except:
            logging_fc("fail")

def manual_selenium_download(date_input, file_name_temp): # manual dload file with input fime name and date
    browser = webdriver.Chrome()
    browser.get(web_linked)
    time.sleep(10)
    try:
        temp = browser.find_element("xpath",box_linked)
        time.sleep(4)
        temp.find_element("xpath", "//*[contains(text(),'"+file_name_temp+"')]").click();
        temp.find_element("xpath",box_date_linked).click()
        time.sleep(4)
        temp.find_element("xpath", "//*[contains(text(),'"+date_input+"')]").click()
        temp.find_element("xpath",button).click()
        logging_fc(file_name_temp)
    except:
        logging_fc("fail")
        

def schedule_job(): # this fc only use in this script
    selenium_download()
    sched = BlockingScheduler()
    sched.configure(max_instances = 2, name='Alternate name')
    @sched.scheduled_job('interval', seconds=time_schedule)
    def ui_schedule():
        selenium_download()
    sched.start()

def thread_schedule_job(): # this multiple threading only use in this script
    t1 = threading.Thread(target = schedule_job())
    t1.start()


if __name__ == "__main__":
    thread_schedule_job()

## python3 backend/selenium_fc.py
