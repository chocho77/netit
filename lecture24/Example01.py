from datetime import datetime, timezone

def current_date_time():
    now = datetime.now()
    print(now.today().date())
    print(now.today().time())
    print()
    print(f"The current day is {now.today().day}.")
    print(f"The current month is {now.today().month}.")
    print(f"The current year is {now.today().year}.")

def main_func():
    print(datetime.now())
    print(datetime.now(timezone.utc))
    print()
    current_date_time()



if __name__ == '__main__':
    main_func()

