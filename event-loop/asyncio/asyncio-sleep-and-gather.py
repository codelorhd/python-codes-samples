# The example given below introduces two new functions:

# asyncio.sleep is the asynchronous implementation of time.sleep. It is a coroutine that sleeps some number of seconds. Since it is a coroutine and not a function, it can be used to yield back the control to the event loop.

# asyncio.gather allows you to wait for several coroutines at once using a single await keyword. Rather than using several sequential await keywords, this allows explicitly stating to the scheduler that all the results of those operations are needed to continue the execution of the program. It ensures that the event loop executes those coroutines concurrently.

# The co-routines run concurrently.

import asyncio


async def hello_world():
    print("hello world!")
    return "Hello World!"


async def hello_python():
    print("hello Python!")
    # Python is not being blocked nor waiting synchronously. This is a coroutine as well.
    await asyncio.sleep(0.1)
    return "Hello Python"


event_loop = asyncio.get_event_loop()
try:
    results: list = event_loop.run_until_complete(
        asyncio.gather(
            hello_world(),
            hello_python(),
        )
    )
    print(results)
finally:
    event_loop.close()
