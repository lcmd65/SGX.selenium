from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from apscheduler.schedulers.blocking import BlockingScheduler
import threading
import time
from backend.string_define import *
from backend.logging_fc import * 


def selenium_download(): # function dload 4 file
    browser = webdriver.Chrome()
    browser.get(web_linked)
    time.sleep(10)
    temp = browser.find_element("xpath",box_linked) #This is a dummy element
    for item_temp in type_of_data:
        try:
            temp1 = temp.find_element("xpath",box_element_linked)
            temp1.click()
            time.sleep(10)
            try:
                temp1.find_element("xpath", "//*[text() = "+item_temp+"]").click();
                logging_fc(item_temp)
            except:
                if item_temp =="Trade Cancellation Data Structure":
                    temp1.find_element("xpath", "//*[text() = 'Trade Cancellation Data Struc...']").click();
                    logging_fc(item_temp)
                else:
                    logging_fc("fail")
            time.sleep(10)
            try:
                temp.find_element("xpath",button).click()
                time.sleep(15)
                temp.find_element("xpath", "//*[text() = 'Download']")
            except:
                temp.find_element("xpath", "//*[text() = 'Download']").click();
                time.sleep(15)
                temp.find_element("xpath", "//*[text() = 'Download']")
        except:
            logging_fc("fail")

def manual_selenium_download(date_input, file_name_temp): # function dload with file name & date input
    browser = webdriver.Chrome()
    browser.get(web_linked)
    try:
        time.sleep(10)
        temp0 = browser.find_element("xpath",box_linked) #This is a dummy element
        time.sleep(10)
        temp1 = temp0.find_element("xpath",box_element_linked)
        temp1.click()
        time.sleep(10)
        temp1.find_element("xpath", "//*[text() = '"+file_name_temp+"']").click();
        time.sleep(10)
        temp2 = temp0.find_element("xpath",box_date_linked)
        temp2.click()
        time.sleep(10)
        temp2.find_element("xpath", "//*[text() = '"+date_input+"']").click()
        time.sleep(10)
        try:
            temp0.find_element("xpath",button).click()
            time.sleep(15)
            temp0.find_element("xpath", "//*[text() = 'Download']")
        except:
            temp0.find_element("xpath", "//*[text() = 'Download']").click();
            time.sleep(15)
            temp0.find_element("xpath", "//*[text() = 'Download']")         
        logging_fc(file_name_temp)
    except:
        logging_fc("fail")

def schedule_job_script(): # this schedule only use in this script
    selenium_download()
    sched = BlockingScheduler()
    sched.configure(max_instances = 4, name='Alternate name')
    @sched.scheduled_job('interval', seconds=time_schedule)
    def ui_schedule():
        selenium_download()
        
    sched.start()

def thread_schedule_job_script(): # this multithread only use in this script
    t1 = threading.Thread(target = schedule_job_script())
    t1.start()


if __name__ == "__main__":
    thread_schedule_job_script()

## python3 backend/selenium_fc.py
