# http.server

## sample

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
        print(path)
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        if path.startswith('/') :
            path = path.lstrip('/')
            
        print(path)
            
        #with open('index.html', 'r') as rfp:
        with open(path, 'r') as rfp:    
            content = rfp.read()
        
        return bytes(content, 'UTF-8')

           
            
if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST, PORT), CallbackServer)
    httpd.serve_forever()

```