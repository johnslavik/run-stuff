import asyncio
import gc
import sys
import weakref

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(asyncio.sleep(0))
loopwr = weakref.ref(loop, lambda wr: print(gc.get_referrers(wr)))

del asyncio, loop
del sys.modules['asyncio']
del sys.modules['_asyncio']

gc.collect()
gc.collect()
gc.collect()
