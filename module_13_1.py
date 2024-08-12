import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 5):
        print(f'Силач {name} поднял {i}')
        await asyncio.sleep(1 / power)
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman("Вася", 10))
    task2 = asyncio.create_task(start_strongman("Петя", 3))
    task3 = asyncio.create_task(start_strongman("Жора", 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())