import asyncio
import time

async def call():

    print('Звонок начался')
    await asyncio.sleep(2)
    print('Звонок закончился')

async def pirin_pos():
    print('Посетитель пришел')
    await asyncio.sleep(2)
    print('Посититель ушел')

async def graffics():
    print('Начало работы с графиками')
    await asyncio.sleep(2)
    print('Графики сделанны')

async def aeroticket():
    print('Выбор авиабилета')
    await asyncio.sleep(5)
    print('Покупка авиабилета')

async def documents():
    print('Заполнение документов началось')
    await asyncio.sleep(5)
    print('Заполнение закончилось')

async def main():
    task_call_aero = asyncio.create_task(call())
    task_pirin = asyncio.create_task(pirin_pos())

    print('9:00')
    await pirin_pos()
    print('10:00')
    await  asyncio.gather(task_call_aero, documents())
    print('11:00')
    await call()
    print('12:00')
    await graffics()
    print('13:00')
    await asyncio.gather(aeroticket(), documents())

asyncio.run(main())