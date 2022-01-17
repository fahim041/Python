import asyncio


async def send_mail():
    print('starting....')
    await asyncio.sleep(2)
    print('finished....')


asyncio.run(send_mail())
