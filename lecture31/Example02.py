import time

#https://realpython.com/python-kwargs-and-args/

def do_something(seconds, *args, **kwargs):
    print(f'Sleeping { seconds } seconds ... ')
    time.sleep(seconds)
    return f'Done sleeping for {seconds} seconds.'

def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result


if __name__ == '__main__':
    print(do_something(5, 3, 1, key='test'))
    

    