from datetime import datetime, timedelta

def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }

def tranfer_date_to_string(datetime_cr):
    switcher = {
        "01": "Jan",
        "02": "Feb",
        "03": "Mar",
        "04": "Apr",
        "05": "May",
        "06": "Jun",
        "07": "Jul",
        "08": "Aug",
        "09": "Sep",
        "10": "Oct",
        "11": "Nov",
        "12": "Dec"
    }
    return switcher.get(datetime_cr, "nothing")
# 
def string_date(date_val):
    datetime_cr = date_val
    string_datetime = datetime_cr.strftime("%d") + " " + \
        tranfer_date_to_string(datetime_cr.strftime("%m")) +" " + \
        datetime_cr.strftime("%Y")
    return string_datetime

def make_last_day(date_val):
    datetime_cr = date_val - timedelta(days=1)
    return datetime_cr

def make_list_datetime_cr():
    list_time = []
    temp_time = datetime.now()
    for i in range (4):
        list_time.append(string_date(temp_time))
        temp_time= make_last_day(temp_time)
    return list_time

def make_time_3day_ago():
    datetime_cr = datetime.now()
    for i in range(3):
        datetime_cr = make_last_day(datetime_cr)
    return string_date(datetime_cr)