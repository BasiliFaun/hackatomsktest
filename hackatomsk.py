import asyncio
import random
import time

async def calc(x):
    bt=time.time()
    await asyncio.sleep(random.uniform(0.0,1.0))
    et=time.time()
    print ("result: {}, time: {}".format(2*x, et-bt))


ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(calc(i)) for i in range(10)]
ioloop.run_until_complete(asyncio.wait(tasks))
ioloop.close()