import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8080

# Evita error de puerto en uso
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Mostrar petición en consola
        termcolor.cprint(self.requestline, 'green')

        # Obtener ruta
        resource = self.path.split('?')[0]

        # 🔹 Ruta principal → HTML
        if resource == "/":
            contents = Path('index.html').read_text()
            content_type = 'text/html'
            error_code = 200

        # 🔹 API REST → devuelve JSON con varias personas
        elif resource == "/listusers":
            contents = Path('people-e1.json').read_text()
            content_type = 'application/json'
            error_code = 200

        # 🔹 Error 404
        else:
            contents = Path('error.html').read_text()
            content_type = 'text/html'
            error_code = 404

        # Enviar respuesta
        self.send_response(error_code)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(contents.encode()))
        self.end_headers()

        self.wfile.write(contents.encode())


# 🔹 Ejecutar servidor
Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at PORT {PORT}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by user")
        httpd.server_close()