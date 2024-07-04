from datetime import datetime, date, time, timedelta

def time_stamp():
    d = datetime.now()
    print(d)
    time_stamp = d.timestamp()
    print(time_stamp)

def delta_time_plus():
    d = datetime.now()
    print("Now")
    print(d)
    print()
    print("135 hours from now.")
    print(d + timedelta(hours=135))
    print()
    print("3 days and 135 hours from now.")
    print(d + timedelta(days=3, hours=135))
    print()
    print("3 days 5 weeks and 135 hours from now.")
    print(d + timedelta(days=3, weeks=5, hours=135))
    print()
    print("10 weeks from now.")
    print(d + timedelta(weeks=10))

def delta_time_minus():
    d = datetime.now()
    print("Now")
    print(d)
    print()
    print("3 days ago.")
    print(d - timedelta(days=3))
    print()
    print("3 weeks ago.")
    print(d - timedelta(weeks=3))

    

def main_func():
    my_day = datetime.now()
    print(my_day.weekday())
    print(my_day.isoweekday())
    print(date(2022, 1, 1), time(13, 22, 15))
    print()
    print()
    time_stamp()
    print()
    delta_time_plus()
    delta_time_minus() 

if __name__ == '__main__':
    main_func()
