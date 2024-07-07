from time import sleep
from multiprocessing import Process

# learn source: https://www.geeksforgeeks.org/how-are-variables-stored-in-python-stack-or-heap/
# https://superfastpython.com/multiprocessing-in-python/

# SuperFastPython.com
# example of running a function in another process

 
# a custom function that blocks for a moment
def task():
    # block for a moment
    sleep(1)
    # display a message
    print('This is from another process')
 
# entry point
if __name__ == '__main__':
    # create a process
    process = Process(target=task)
    # run the process
    process.start()
    # wait for the process to finish
    print('Waiting for the process...')
    process.join()