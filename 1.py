# import asyncio
# import time
#
#
# async def async_func(num):
#     print(f'...start {num}')
#     await asyncio.sleep(3)
#     print(f'...end {num}')
#
# async def main():
#     taskA = asyncio.create_task(async_func('A'))
#     taskB = asyncio.create_task(async_func('B'))
#     taskC = asyncio.create_task(async_func('C'))
#     await asyncio.wait([taskA, taskB, taskC])
#
# if __name__ == '__main__':
#     asyncio.run(main())
# import asyncio
#
# async def count(counter):
#     print(f'Кол-во записей в списке {len(counter)}')
#     while True:
#         await asyncio.sleep(1/1000)
#         counter.append(1)
#
# async def print_every_sec(counter):
#     while True:
#         await asyncio.sleep(1)
#         print(f'прошла 1 секунда. Элементов в списке {len(counter)}')
#
# async def print_every_5sec():
#     while True:
#         await asyncio.sleep(5)
#         print(f'прошло 5 секунд')
#
# async def print_every_10sec():
#     while True:
#         await asyncio.sleep(10)
#         print(f'прошло 10 секунд')
#
# async def main():
#     counter = []
#     task1 = asyncio.create_task(count(counter))
#     task2 = asyncio.create_task(print_every_sec(counter))
#     task3 = asyncio.create_task(print_every_5sec())
#     task4 = asyncio.create_task(print_every_10sec())
#
# asyncio.run(main())

# import time
# import asyncio
#
# async def MakeCoffe():
#     print('start makeCoffe')
#     time.sleep(3)
#     print('end makeCoffe')
#     return 'Coffe is ready'
#
# async def toastBrew():
#     print('start toastbrev')
#     time.sleep(2)
#     print('end toastBrew')
#     return 'toasts is ready'
#
# async def main():
#     start = time.time()
#     await asyncio.gather(MakeCoffe(), toastBrew())
#     end = time.time()
#     print(f'Времени прошло: {end-start:.2f} секунд')
#
# if __name__ == '__main__':
#     asyncio.run(main())

import asyncio
async def my_sleep():
    print('sleep start')
    await asyncio.sleep(3)
    print('sleep end')

async def my_work():
    print('work start')
    await asyncio.sleep(3)
    d = 2+3
    print('work end')

async def main():
    task1 = asyncio.create_task(my_sleep())
    task2 = asyncio.create_task(my_work())
    print('rest start')
    await task1
    print('rest end')
    await task2

asyncio.run(main())