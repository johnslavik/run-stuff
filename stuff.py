import asyncio
import gc
import weakref

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(asyncio.sleep(0))
loopwr = weakref.ref(loop, lambda wr: print(gc.get_referrers(wr)))

del asyncio, loop

gc.collect()
gc.collect()
gc.collect()
