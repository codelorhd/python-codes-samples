# The aiohttp library provides an asynchronous HTTP
import asyncio
import aiohttp


async def get(url):
    # Note: The async with keyword used in the example is equivalent to the await keyword, but it is specific to context managers that use await in their enter and exit methods
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response


loop = asyncio.get_event_loop()
# This example creates several coroutines, one for each call. Those coroutines are then gathered, and so they are executed concurrently by the event loop. If the remote web server is far away and needs a long delay to reply, the event loop switches to the next coroutine that is ready to be resumed, making sure the connections are ready to be read.
coroutines = [get("http://example.com") for _ in range(8)]
results = loop.run_until_complete(asyncio.gather(*coroutines))

print("Results: %s" % results)
