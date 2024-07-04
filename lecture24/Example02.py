from datetime import datetime

def create_date_time():
    d = datetime(2001, 5, 3, 13, 15, 30, 123534)
    print(f"Created date time : {d}")

    d2 = datetime.fromtimestamp(1720073533 + 3600)
    print(f"From Unix Time Stamp : {d2}")


def formated_date_time():
    now = datetime.now()

    print(f"{now.today().day}/{now.today().month}/{now.today().year}")
    print(f"seconds : {now.time().second}, microsecond : {now.time().microsecond}")

def main_func():
    formated_date_time()
    create_date_time()



if __name__ == '__main__':
    main_func()