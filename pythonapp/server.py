from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
import app
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/posts':
            posts = app.handle_get_posts()
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(posts).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/add':
            length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(length)
            data = urlparse.parse_qs(post_data.decode())
            title = data.get('title')[0]
            content = data.get('content')[0]
            try:
                app.handle_add_post(title, content)
                self.send_response(200)
            except ValueError as e:
                self.send_response(400)
                self.wfile.write(str(e).encode())
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    database.init_db()
    run()
