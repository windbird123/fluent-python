import asyncio


async def download():
    print('download document')


async def log():
    print('log to file')


async def main():
    # 2. using wait
    await download()

    # 3. create_task
    asyncio.create_task(log())


# 1. using asyncio
asyncio.run(main())
