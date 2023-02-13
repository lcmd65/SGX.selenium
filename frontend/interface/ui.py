from functools import partial
from tkinter.ttk import *
from tkinter import *
from tkinter import StringVar
from frontend.function.function_ui import *

# function interaction ui

def click_run_root_temp(): # env static val processing for auto loop
    global state_in_root_temp
    global signal_loop
    state_in_root_temp = 'run'
    signal_loop = 1
    messagebox.showinfo(title= "Message", message="Start auto")

def click_exit_root_temp(): # exit button fucnton in auto frame
    global state_in_root_temp
    global signal_loop
    state_in_root_temp = 'end'
    signal_loop = 0
    
def start_loop(): # loop function schedule
    global state_in_root_temp 
    global signal_loop
    if state_in_root_temp == "run":
        state_check_thread()
    if signal_loop == 1:
        root.after(time_schedule,sequence(partial(start_loop), loop))

def clicked_function_app_schedule(): # init auto frame by click button
    global state_in_root_temp
    global signal_loop
    signal_loop = 1
    root_temp= Tk()
    root_temp.geometry("400x80+300+300")
    app_temp = Checking_running(root_temp)
    start_loop()
    root_temp.mainloop()

class Example(Frame): # main frame
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("MINI PROJECT")
        self.pack(fill=BOTH, expand=True)
        
        date_var = StringVar()
        file_var = StringVar()
        # P3AB
        frame1a = Frame(self)
        frame1a.pack(fill=X)
        frame2a = Frame(self)
        frame2a.pack(fill=X)
        frame3a = Frame(self)
        frame3a.pack(fill=X)
        frame4a = Frame(self)
        frame4a.pack(fill=BOTH)
        
        label = Label(frame2a, text = "Date Time",width= 15 )
        label.pack(side = LEFT)
        txt = Entry(frame2a, textvariable = date_var)
        txt.insert(0, make_time_3day_ago())
        txt.pack(fill=BOTH, pady=0, padx=5, expand=True)
        
        label2 = Label(frame3a, text = "File Name", width=15 )
        label2.pack(side = LEFT)
        txt2 = Entry(frame3a, textvariable=file_var)
        txt2.insert(0, type_of_data[0])
        txt2.pack(fill=BOTH, pady=0, padx=5, expand=True)
        
        Button_tab1_0 = Button(frame1a, text="MANUAL DOWNLOAD", width=20, command = partial(manual_function,txt,txt2))
        Button_tab1_0.pack(side=LEFT, padx=5, pady=5)
        Button_tab1_1 = Button(frame4a, text="AUTO SCHEDULE", width=20, command = clicked_function_app_schedule)
        Button_tab1_1.pack(side=RIGHT, padx=5, pady=30)


class Checking_running(Frame): # auto running frame
    def __init__(self, parent): 
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("PROJECT AUTO RUNNING")
        self.pack(fill=BOTH, expand=True)
        
        frame1 = Frame(self)
        frame1.pack(fill = X)
        frame2 = Frame(self)
        frame2.pack(fill= BOTH)
        
        Button1 = Button(frame1, text ="Run",width =15, command = click_run_root_temp )
        Button1.pack(side = BOTTOM, padx =5, pady=5)
        
        Button2 = Button(frame2, text="End", width =5, command = sequence(click_exit_root_temp, exit))
        Button2.pack(side = RIGHT, padx=5, pady =5)

if __name__ == "__main__" :
    root = Tk()
    root.geometry('600x400+200+200') 
    app= Example(root)
    root.mainloop()
    
# python3 frontend/interface/ui.py
