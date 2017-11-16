import asyncio
import random

async def calc(x):
    await asyncio.sleep(random.uniform(0.0,1.0))
    return 2*x

async def asynchronous():
    futures = [calc(i) for i in range(10)]
    done, _ = await asyncio.wait(futures)
    #for task in done:
    #    print(task.result())
    for future in sorted(done,key=lambda x: x.result()):
        print(future.result())

ioloop = asyncio.get_event_loop()

ioloop.run_until_complete(asynchronous())
ioloop.close()