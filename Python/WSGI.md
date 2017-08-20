# WSGI

## サンプルコード(Python 3.x)
``` python
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    ret = [("%s: %s\n" % (key, value)).encode("utf-8")
           for key, value in environ.items()]
    return ret

with make_server('', 8080, simple_app) as httpd:
    print("Serving on port 8080...")
    httpd.serve_forever()
```

```
$ python ./test_server.py 

```

### テストサーバー（WSGIなのか？）

``` python
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = 'localhost'
PORT = 8080

class CallbackServer(BaseHTTPRequestHandler):
    def construct_path_dict(self):
        print("construct_path_dict")
        self.path_dict = {}
        
    def __init__(self, request, client_address, server):
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)
        self.construct_path_dict()

    def do_GET(self):
        response = self.handle_http(self.path)
        self.wfile.write(response)

    def handle_http(self,  path):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        if path.startswith('/') :
            path = path.lstrip('/')
            
        print(path)

        with open(path, 'r') as rfp:    
            content = rfp.read()
        
        return bytes(content, 'UTF-8')
        
            
if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST, PORT), CallbackServer)
    httpd.serve_forever()
    
```



[参考]
[WSGI](https://docs.python.jp/3/library/wsgiref.html)

