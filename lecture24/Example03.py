from datetime import datetime
from dateutil.parser import parse

def main_func():
    print(parse("01 02 2022 13:52:32"))

    d = datetime.strptime("01 02 2022", "%d %m %Y")
    d1 = datetime.strptime("01 02 2023 15:03:32", "%d %m %Y %H:%M:%S")
    my_date = datetime.now()
    print(f"ISO format : {my_date.strftime('%Y-%m-%dT%H:%M:%S.%f%z')}")  # ISO Format
    print(d)
    print(d1)

if __name__ == '__main__':
    main_func()

