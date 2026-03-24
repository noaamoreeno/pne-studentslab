from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/info/A":
            file = open("html/info/A.html")
        elif self.path == "/info/C":
            file = open("html/info/C.html")
        else:
            self.send_response(200)
            self.end_headers()
            return

        content = file.read()
        file.close()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(content.encode())

server = HTTPServer(("localhost", 8080), MyHandler)
server.serve_forever()