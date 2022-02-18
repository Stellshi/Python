from email import message
from http.server import HTTPServer, BaseHTTPRequestHandler
from unicodedata import name

APP_HOST = 'localhost'
APP_PORT = 8000


class SimpleGetHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type','text/html;charset-utf-8')
        self.end_headers()
        
    def _html(self,message):
        content=(f"<html>"
                 "<body>"
                 "<h1>{message}<\h1>"
                 "</body>"
                 "</html>")
        return content.encode('utf-8')
    
    def do_Get(self):
        self._set_headers()
        message= 'Привет мир!'
        self.wfile.write(self._html(message))
        
def run_server(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_adress = (APP_HOST,APP_PORT)
    httpd=server_class(server_adress,handler_class)
    httpd.serve_forever()
    
if __name__ == '__main__':
    run_server(handler_class=SimpleGetHandler)
        