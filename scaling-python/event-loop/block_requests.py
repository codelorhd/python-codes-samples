import socket

s = socket.create_connection(("httpbin.org", 80))
s.send(b"GET /delay/5 HTTP/1.1\r\nHost: httpbin.org\r\n\r\n")
buf = s.recv(1024)
print(buf)

# ** Solution,
# This will give an error because it is not blocking and
# the resource is not immediately available when it is requested.
import socket

s = socket.create_connection(("httpbin.org", 80))
s.setblocking(False)
s.send(b"GET /delay/5 HTTP/1.1\r\nHost: httpbin.org\r\n\r\n")
buf = s.recv(1024)
print(buf)
