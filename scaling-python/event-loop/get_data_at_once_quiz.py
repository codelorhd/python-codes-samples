# When a webpage loads, its base HTML page has a bunch of resources that the browser needs to fetch in order to display the page completely. However, the time that the browser takes to fetch all those resources determines its quality.

# In this challenge, suppose you are writing code for building a browser. You have to fetch three URLs: http://educative.io, http://educative.io/blog, and http://youtube.com.

import aiohttp
import asyncio

urls = ["http://educative.io", "http://educative.io/blog", "http://youtube.com"]

##########################################
### Start your code here
async def get(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response


# define a loop
loop = asyncio.get_event_loop()
corountines = [get(url) for url in urls]
results = loop.run_until_complete(asyncio.gather(*corountines))

### End code here
##########################################
print("Results: %s" % results)
