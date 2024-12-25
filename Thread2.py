import time
import threading


def thread1():
    for i in range(5):
        print("Thread 1")
        time.sleep(1)


def thread2():
    for i in range(5):
        print("Thread 2")
        time.sleep(1)

if __name__ == '__main__':
    start_time = time.time()
    

    thread1()
    thread2()

    time_taken = time.time()- start_time
    print(f"start time: {start_time}")
    print(f"time taken: {time_taken} seconds")