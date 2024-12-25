import time
import multiprocessing
import asyncio

async def thread1():
    for i in range(5):
        print("Thread 1 running")
        await asyncio.sleep(1)


async def thread2():
    for i in range(5):
        print("Thread 2 running")
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(thread1(), thread2())

if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())

    time_taken = time.time()- start_time
    print(f"start time: {start_time}")
    print(f"time taken: {time_taken} seconds")
