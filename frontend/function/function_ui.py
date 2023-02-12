import threading
from tkinter import messagebox
from backend.selenium_fc import *

state_in_root_temp = 'end'

def state_check_thread():
    t1 = threading.Thread(target=state_check(), )
    t1.start()
    t1.join()
    
def state_check():
    try:
        processing_fc()
    except:
        messagebox.showinfo(title= "Message", message ="Error in connect")

##_________Running 2+ funtion in event
def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

def processing_fc():
    selenium_download() ## no use schedule in this ui function