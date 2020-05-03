import asyncio
loop = asyncio.get_event_loop()


async def hello1():
    print("hello")
    await asyncio.sleep(3)
    print("world")


@asyncio.coroutine
def hello():
    print("hello")
    yield from asyncio.sleep(3)
    print("world")

    
if __name__ == '__main__':
    loop.run_until_complete(hello())