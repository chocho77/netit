from time import sleep
from random import random
from concurrent.futures import ThreadPoolExecutor

# https://superfastpython.com/threadpoolexecutor-submit/
# https://superfastpython.com/threadpoolexecutor-map/
# https://ipython.ai/practical-threading-python-guide/
# https://superfastpython.com/python-asynchronous-programming/
# https://superfastpython.com/multiprocessing-in-python/

# SuperFastPython.com
# example of calling map and processing results

 
# custom task that will sleep for a variable amount of time
def task(name):
    # sleep for less than a second
    sleep(random())
    return f'Task: {name} done.'
 
# start the thread pool
with ThreadPoolExecutor(10) as executor:
    # execute tasks concurrently and process results in order
    for result in executor.map(task, range(10)):
        # report the result
        print(result)