import asyncio


async def download(urls):
    for url in urls:
        await asyncio.sleep(1)
        response = {'status': 200, 'data': f'content of {url}'}

        if url == 'naver.com':
            response['status'] = 500

        yield response


async def handle(error_response):
    print('logging error for ', error_response)


async def main():
    urls = [
        'google.com',
        'naver.com'
    ]

    errors = [r async for r in download(urls) if r['status'] != 200]
    print(errors)

    [await handle(e) for e in errors]


asyncio.run(main())
