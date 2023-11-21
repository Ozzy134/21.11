import time
import httpx
import asyncio

async def download(current):
    url = f'https://reqres.in/api/users/{current}'

    async with httpx.AsyncClient() as client:
        result = await client.get(url)
        if result.status_code == 200:
            my_res = result.json()
            print_info(my_res.get('data'))
        else:
            print(result.status_code)
        print(f'Результат №{current}')

def print_info(info):
    print(f"Имя {info['first_name']}, фамилия {info['last_name']}")

async def main():
    users_count = int(input('Сколько человек: '))

    current = 0
    while current < users_count:
        current += 1
        task = asyncio.create_task(download(current))
        await task
    print('Done')

asyncio.run(main())