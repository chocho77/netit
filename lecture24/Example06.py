from datetime import datetime
import pytz

def main_func():
    d = datetime.now()
    print("Now")
    print(d)
    print("UTC Time")
    print(d.astimezone(pytz.UTC))
    d = datetime(2001, 5, 3, 12, 22, 33, tzinfo=pytz.timezone('Pacific/Galapagos'))
    print("Pacific/Galapagos")
    print(d)
    print("UTC Time")
    print(d.astimezone(pytz.UTC))
    print("Now time in timezone: Antarctica/DumontDUrville")
    print(d.now(tz=pytz.timezone("Antarctica/DumontDUrville")))

if __name__ == '__main__':
    main_func()
