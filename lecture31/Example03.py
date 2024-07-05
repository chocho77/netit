from time import sleep, perf_counter

# https://www.pythontutorial.net/python-concurrency/python-threading/


def task():
    print('Starting a task...')
    sleep(1)
    print('done')


start_time = perf_counter()

task()
task()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
