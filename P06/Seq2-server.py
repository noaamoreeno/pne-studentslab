from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

SEQUENCES = [
    "ATCG",
    "GGTA",
    "CCTA",
    "TATA",
    "GCGC"
]

GENES = {
    "U5": "ATCGATCG",
    "ADA": "GGGAAA",
    "FRAT1": "TTTCCC",
    "FXN": "AACCGG",
    "RNU6_269P": "GATTACA"
}


def complement(seq):
    comp = ""
    for base in seq:
        if base == "A":
            comp += "T"
        elif base == "T":
            comp += "A"
        elif base == "C":
            comp += "G"
        elif base == "G":
            comp += "C"
    return comp


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        params = urllib.parse.parse_qs(parsed.query)

        if path == "/":
            file = open("html/index.html")

        elif path == "/ping":
            content = "<h1>Server alive</h1><a href='/'>Back</a>"
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode())
            return

        elif path == "/get":
            n = int(params.get("n", [0])[0])
            seq = SEQUENCES[n]
            content = f"<h1>Sequence: {seq}</h1><a href='/'>Back</a>"

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode())
            return

        elif path == "/gene":
            name = params.get("name", [""])[0]
            seq = GENES.get(name, "Not found")

            content = f"<h1>{name}: {seq}</h1><a href='/'>Back</a>"

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode())
            return

        elif path == "/operation":
            seq = params.get("seq", [""])[0]
            op = params.get("op", [""])[0]

            if op == "info":
                total = len(seq)
                a = seq.count("A")
                c = seq.count("C")
                g = seq.count("G")
                t = seq.count("T")

                content = f"""
                <p>Sequence: {seq}</p>
                <p>Total length: {total}</p>
                <p>A: {a}</p>
                <p>C: {c}</p>
                <p>G: {g}</p>
                <p>T: {t}</p>
                <a href='/'>Back</a>
                """

            elif op == "comp":
                content = f"<p>{complement(seq)}</p><a href='/'>Back</a>"

            elif op == "rev":
                content = f"<p>{seq[::-1]}</p><a href='/'>Back</a>"

            else:
                content = "Invalid operation"

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode())
            return

        else:
            file = open("html/error.html")

        content = file.read()
        file.close()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(content.encode())


server = HTTPServer(("localhost", 8080), Handler)
print("Running on http://127.0.0.1:8080/")
server.serve_forever()