import time
import asyncio

async def summ(a, b):
    await asyncio.sleep(1)
    print(a + b)

async def slow(a, b):
    await asyncio.sleep(3)
    print(a * b)

async def main():
    start = time.time()
    task1 = asyncio.create_task(summ(1, 2))
    task2 = asyncio.create_task(slow(5, 5))
    await task1
    await task2
    en = time.time()
    print(start + en)

asyncio.run(main())