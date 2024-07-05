from time import sleep, perf_counter
from threading import Thread

# https://www.pythontutorial.net/python-concurrency/python-threading/

def task():
    print('Starting a task...')
    sleep(1)
    print('done')

if __name__ == '__main__':
    start_time = perf_counter()

    # create two new threads
    thread_new_one = Thread(target=task)
    thread_new_two = Thread(target=task)

    # start the threads
    thread_new_one.start()
    thread_new_two.start()

    # wait for the threads to complete
    thread_new_one.join()
    thread_new_two.join()

    end_time = perf_counter()

    print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')