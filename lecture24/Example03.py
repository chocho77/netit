from datetime import datetime
from dateutil.parser import parse

def main_func():
    print(parse("01 02 2022 13:52:32"))

    d = datetime.strptime("01 02 2022", "%d %m %Y")
    d1 = datetime.strptime("01 02 2023 15:03:32", "%d %m %Y %H:%M:%S")
    d2 = datetime.strptime("2018-01-02T22:10:05.284208", "%Y-%m-%dT%H:%M:%S.%f")  # ISO Time Format without %z otherwise rise a error 
    print(type(d2))
    d2_to_str = d2.strftime("%d %m %Y %H:%M:%S")
    print(d2_to_str)
    print(type(d2_to_str))
    my_date = datetime.now()
    my_date_to_str = my_date.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
    print(f"ISO format : {my_date_to_str}")  # ISO Time Format
    print(type(my_date_to_str))
    
    print(d)
    print(d1)
    print(d2)

if __name__ == '__main__':
    main_func()

