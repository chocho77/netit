import time
import os
from multiprocessing import Process

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    return f"Done Sleeping ... {seconds}"

if __name__ == "__main__":
    start = time.perf_counter()

    cpu_count = os.cpu_count()
    print(f"CPU cores count: {cpu_count}")

    processes = []

    for _ in range(cpu_count):
        process = Process(target=do_something, args=[1.5])
        process.start()

        processes.append(process)

    time.sleep(200)

    for process in processes:
        process.join()
    
    finish = time.perf_counter()

    print(f"Finished in {round(finish - start, 2)} second(s)")

    

