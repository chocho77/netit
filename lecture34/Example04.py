from multiprocessing import Process

#The example below creates an instance of a multiprocessing.Process and reports the assigned PID.

# SuperFastPython.com
# example of reporting the native process identifier
# entry point
if __name__ == '__main__':
    # create the process
    process = Process()
    # report the process identifier
    print(process.pid)
    # start the process
    process.start()
    # report the process identifier
    print(process.pid)