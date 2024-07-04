from datetime import datetime

def main_func():
    print(datetime.now())
    print(datetime.now().year)
    print(datetime.now().month)
    print(datetime.now().strftime("%W"))
    print(datetime.now().weekday())
    print(datetime.now().strftime("%j"))    # for more code: https://strftime.org
    print(datetime.now().strftime("%d"))    # for more info: https://strftime.org
    print(datetime.now().strftime("%A"))    # for more info: https://strftime.org
    pass

if __name__ == '__main__':
    main_func()

