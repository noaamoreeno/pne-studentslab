from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/info/A":
            file = open("html/info/A.html")
            content = file.read()
            file.close()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(content.encode())
        else:
            self.send_response(200)
            self.end_headers()

server = HTTPServer(("localhost", 8080), MyHandler)
print("Server running...")
server.serve_forever()