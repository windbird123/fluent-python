import asyncio

tasks = [1, 2, 3, 4, 5, 6, 7, 8]
sem = asyncio.Semaphore(2)


async def run_task(x):
    async with sem:
        print(f"task start: {x}")
        await asyncio.sleep(1)
        print(f"task end: {x}")
        return x * 2


async def main():
    coros = [run_task(x) for x in tasks]
    await asyncio.gather(*coros)


asyncio.run(main())
