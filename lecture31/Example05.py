from threading import Thread

def print_something():
    print("Print something.")

if __name__ == '__main__':
    thread_one = Thread(target=print_something)
    thread_one.start()
    print(f"Thread Name :{thread_one.getName()}")
    print(f"Thread Ident : {thread_one.ident}")
    print(f"Thread is_alive : {thread_one.is_alive()}")
    print(f"Thread Native Id : {thread_one.native_id}")
    thread_two = Thread(target=print_something)
    thread_two.start()
    print(f"Thread Name :{thread_two.getName()}")
    print(f"Thread Ident : {thread_two.ident}")
    print(f"Thread is_alive : {thread_two.is_alive()}")
    print(f"Thread Native Id : {thread_two.native_id}")





