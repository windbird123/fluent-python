import asyncio

tasks = [1, 2, 3, 4, 5, 6, 7, 8]
sem = asyncio.Semaphore(2)


async def run_task(x):
    async with sem:
        print(f"task start: {x}")
        await asyncio.sleep(1)
        print(f"task end: {x}")
        return x * 2


async def main_old():
    coros = [run_task(x) for x in tasks]
    await asyncio.gather(*coros)

async def main():
    tracks = []

    try:
        async with asyncio.TaskGroup() as tg:
            for x in tasks:
                t = tg.create_task(run_task(x))
                tracks.append(t)
    except* Exception as eg:
        for exc in eg.exceptions:
            print(f"task 예외: {exc!r}")

    results = [t.result() for t in tracks if not t.cancelled() and t.exception() is None]
    print(results)

asyncio.run(main())
