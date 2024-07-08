from time import sleep
from concurrent.futures import ThreadPoolExecutor


# https://superfastpython.com/threadpoolexecutor-submit/
# https://superfastpython.com/threadpoolexecutor-map/
# https://ipython.ai/practical-threading-python-guide/
# https://superfastpython.com/python-asynchronous-programming/
# https://superfastpython.com/multiprocessing-in-python/


# SuperFastPython.com
# example of using the thread pool with a context manager

 
# mock test that works for moment
def task(name):
    sleep(0.5)
    return name
 
# start the thread pool
with ThreadPoolExecutor(10) as executor:
    # submit tasks and process results
    for result in executor.map(task, range(10)):
        # report the result
        print(f'Task done: {result}')
    # thread pool is shutdown automatically
# all done, continue on
print('Done!')