import asyncio
import time

# https://www.slingacademy.com/article/python-3-11-asyncio-streamwriter-a-practical-guide-with-examples/

async def count():
    await asyncio.sleep(1)
    print('1')
    await asyncio.sleep(1)
    print('2')
    await asyncio.sleep(1)
    print('3')

async def main():
    tasks = []
    for i in range(200):
        task = asyncio.create_task(count())
        tasks.append(task)
    
    for task in tasks:
        await task

if __name__ == '__main__':
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f'Total time : {total_time:0.2f} seconds.')
