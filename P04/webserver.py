from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            path = "html/index.html"
        elif self.path == "/info/A":
            path = "html/info/A.html"
        elif self.path == "/info/C":
            path = "html/info/C.html"
        elif self.path == "/info/G":
            path = "html/info/G.html"
        elif self.path == "/info/T":
            path = "html/info/T.html"
        else:
            path = "html/error.html"

        file = open(path)
        content = file.read()
        file.close()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(content.encode())

server = HTTPServer(("localhost", 8080), MyHandler)
print("Server running on http://127.0.0.1:8080/")
server.serve_forever()