import threading

# source: https://ipython.ai/practical-threading-python-guide/

# Shared resource
counter = 0

# Lock object
lock = threading.Lock()

# Target function for threads
def increment_counter():
    global counter
    for _ in range(100000):
        # Acquire lock before accessing the shared resource
        lock.acquire()
        try:
            counter += 1
        finally:
            # Ensure the lock is always released
            lock.release()

# Creating threads
threads = [threading.Thread(target=increment_counter) for _ in range(10)]

# Starting threads
for thread in threads:
    thread.start()

# Waiting for all threads to complete
for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")