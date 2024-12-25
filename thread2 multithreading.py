import time
import multiprocessing
import threading


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
    
   
    tr1 = threading.Thread(target=thread1, daemon= True)
    tr2 = threading.Thread(target=thread2, daemon= True)

    tr1.start()
    tr2.start()

    tr1.join(5)
    tr2.join(6)

    time_taken = time.time()- start_time
    print(f"start time: {start_time}")
    print(f"time taken: {time_taken} seconds")
