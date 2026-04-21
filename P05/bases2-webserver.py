import http.server
import socketserver
from pathlib import Path

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


class MyHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        print("Request:", self.path)

        if self.path == "/" or self.path == "/index.html":
            file_path = Path("html/index.html")

        else:

            requested_file = self.path.lstrip("/")
            file_path = Path("html") / requested_file

        try:

            with open(file_path, "rb") as f:
                content = f.read()

            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", len(content))
            self.end_headers()

            self.wfile.write(content)

        except FileNotFoundError:
            # If file doesn't exist → send error.html
            with open("html/error.html", "rb") as f:
                content = f.read()

            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", len(content))
            self.end_headers()

            self.wfile.write(content)

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Serving at port", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
        httpd.server_close()