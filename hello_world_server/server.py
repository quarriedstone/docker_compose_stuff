import http.server
import socketserver
from http import HTTPStatus
import redis

IP="0.0.0.0"
PORT=8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        r.incr("counter")
        i = r.get("counter").decode("utf-8")
        self.wfile.write(f'Hello world\n Number of visitors: {i}\n'.encode('utf-8'))

r = redis.Redis()
httpd = socketserver.TCPServer((IP, PORT), Handler)
httpd.serve_forever()


# python3 server.py
# 127.0.0.1 - - [11/Apr/2017 11:36:49] "GET / HTTP/1.1" 200 -
# http :8000
'''
HTTP/1.0 200 OK
Date: Tue, 11 Apr 2017 15:36:49 GMT
Server: SimpleHTTP/0.6 Python/3.5.2
Hello world
'''
