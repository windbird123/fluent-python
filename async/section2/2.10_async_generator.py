import asyncio


async def download(urls):
    for url in urls:
        await asyncio.sleep(1)
        response = {'status': 200, 'data': f'content of {url}'}
        yield response


async def main():
    urls = [
        'google.com',
        'naver.com'
    ]

    async for value in download(urls):
        print(value)


asyncio.run(main())
