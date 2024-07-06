import concurrent.futures
import time

def do_something(*args, **kwargs):
    raise Exception('Something bad happend')
    return 'String'

def callback_function(future_object):
    _exception_raised = future_object.exception()
    print('Callback was called')

if __name__ == '__main__':
    start = time.perf_counter()

    threads_count = 20
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads_count) as executor:
        number_of_args = 4
        secs = [i for i in range(number_of_args)]

        futures = []
        future =executor.submit(do_something, secs)
        future.add_done_callback(callback_function)
        futures.append(future)

        for future in futures:
            exception_rised = future.exception()
            if exception_rised:
                print(f'Exception was raised: {exception_rised}')
            
            try:
                result = future.result()
            except Exception as exception:
                result = f'Gave up on result. Error: {exception}'

            print(result)
                

            print(future.result())