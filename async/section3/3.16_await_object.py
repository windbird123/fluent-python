import asyncio


# python 의 Awaitable:
#  - 1. coroutine
#  - 2. task
#  - 3. future
#  - 4. 혹은 Awaitable class 를 만들수도 있음

class Stopwatch:
    def __await__(self):
        yield


async def main():
    await Stopwatch()


asyncio.run(main())
