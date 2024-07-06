# SuperFastPython.com
# example of calling map and waiting for all tasks to complete
from time import sleep
from random import random
from concurrent.futures import ThreadPoolExecutor
 
# custom task that will sleep for a variable amount of time
def task(value):
    # sleep for less than a second
    sleep(random())
    print(f'Done: {value}')
 

# start the thread pool
with ThreadPoolExecutor() as executor:
    # submit all tasks
    executor.map(task, range(5))
    # shutdown, wait for all tasks to complete
    print('Waiting...')
print('All done.')