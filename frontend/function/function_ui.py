import threading
from tkinter import messagebox
from pipe.pipe import * # BE function

signal_loop = 1
state_in_root_temp = 'end'

# function interaction ui
def loop():
    print("loop")
    
def get_date_input(entry_cr):
    date = entry_cr.get()
    return date

def get_file_input(entry_cr):
    file = entry_cr.get()
    return file

def manual_function(entry1, entry2):
    manual_selenium_download(get_date_input(entry1), get_file_input(entry2))

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