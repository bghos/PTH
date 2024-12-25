import time
import multiprocessing


def thread1():
    for i in range(5):
        print("Thread 1 running")
        time.sleep(1)


def thread2():
    for i in range(5):
        print("Thread 2 running")
        time.sleep(1)

if __name__ == '__main__':
    start_time = time.time()
    

    # thread1()
    # thread2()

    
    process1 = multiprocessing.Process(target=thread1)
    process2 = multiprocessing.Process(target=thread2)

    process1.start()
    process2.start()

    process1.join(5)
    process2.join(6)

    time_taken = time.time()- start_time
    print(f"start time: {start_time}")
    print(f"time taken: {time_taken} seconds")
