import asyncio


class EggBoiler:
    def __init__(self, amount: int):
        self.eggs = range(1, amount + 1)
        self.current = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current < len(self.eggs):
            value = self.eggs[self.current]
            self.current += 1
            return value
        else:
            raise StopAsyncIteration


async def boil(egg):
    await asyncio.sleep(1)
    print(f"boiling #{egg}")


async def main():
    tasks = []
    async for egg in EggBoiler(4):
        tasks.append(asyncio.create_task(boil(egg)))

    await asyncio.gather(*tasks)


asyncio.run(main())
