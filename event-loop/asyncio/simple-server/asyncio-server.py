# Note: It is possible to build an asyncio based Web server using aiohttp. However, it is not that useful in most cases because it will often be slower than a fast, optimized, native WSGI server like uwsgi or gunicorn. Beacuse Python Web applications are always using WSGI, it is easy to switch out the WSGI server for a fast and asynchronous one.


import asyncio

SERVER_ADDRESS = ("0.0.0.0", 1234)


class YellEchoServer(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        print("Connection received from:", transport.get_extra_info("peername"))

    def data_received(self, data):
        print("Receiving", data)
        self.transport.write(data.upper())

    def connection_lost(self, exc):
        print("Client disconnected")


event_loop = asyncio.get_event_loop()

factory = event_loop.create_server(YellEchoServer, *SERVER_ADDRESS)

# Runs the yell server so it is waiting for requests
# Runs this, till a future is done, e.g. server is closed.
server = event_loop.run_until_complete(factory)

try:
    # Run this forever, meaning keep running and waiting
    event_loop.run_forever()
    print("Server started")
finally:
    server.close()
    event_loop.run_until_complete(server.wait_closed())
    event_loop.close()
