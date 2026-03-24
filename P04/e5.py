from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path == "/info/A":
                file = open("html/info/A.html")
            elif self.path == "/info/C":
                file = open("html/info/C.html")
            elif self.path == "/info/G":
                file = open("html/info/G.html")
            elif self.path == "/info/T":
                file = open("html/info/T.html")
            else:
                file = open("html/error.html")

            content = file.read()
            file.close()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(content.encode())

        except:
            self.send_response(500)
            self.end_headers()

server = HTTPServer(("localhost", 8080), MyHandler)
server.serve_forever()