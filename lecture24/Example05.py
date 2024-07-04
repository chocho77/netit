from datetime import datetime
import pytz

def main_func():
    
    print(pytz.all_timezones)
    print(len(pytz.all_timezones))

    print()
    d = datetime.now()
    print(d.astimezone(pytz.timezone("US/Arizona")))
    print()
    print(d.astimezone(pytz.timezone("Europe/Rome")))
    print()
    print()
    print(d.astimezone(pytz.UTC))


if __name__ == '__main__':
    main_func()