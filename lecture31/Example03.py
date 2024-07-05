import time
# https://www.pythontutorial.net/python-concurrency/python-threading/

def do_something(seconds, *args, **kwargs):
    print(f'Sleeping { seconds } seconds ... ')
    time.sleep(seconds)
    return f'Done sleeping for {seconds} seconds.'

if __name__ == '__main__':
    start_time = time.perf_counter()

    with concurrent.