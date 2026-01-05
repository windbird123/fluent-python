import asyncio


async def stopwatch():
    count = 0
    while count < 4:
        await asyncio.sleep(1)
        count += 1
        print(f"count: {count}")


def callback(task):
    print('task is done', task)

async def main():
    task = asyncio.create_task(stopwatch())
    task.add_done_callback(callback)
    await task

asyncio.run(main())
