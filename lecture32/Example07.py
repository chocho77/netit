import threading
import time

def do_something(seconds):
    print(f"I will do something for {seconds}")
    time.sleep(seconds)
    return f"I have slept for {seconds}"

if __name__ == "__main__":
    start = time.perf_counter()

    count_threads = 20
    threads = []

    for _ in range(count_threads):
        thread = threading.Thread(target=do_something, args=[1.5])
        thread.start()
        threads.append(thread)

    finish = time.perf_counter()

    print(f"Finished in {round(finish - start, 2)} second(s)")

