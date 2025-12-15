import asyncio
import gc
import weakref

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(asyncio.sleep(0))
loopwr = weakref.ref(loop)

del asyncio, loop

print(gc.get_referrers(loopwr()))
