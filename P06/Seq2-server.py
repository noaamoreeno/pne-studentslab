from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

SEQUENCES = ["ATCG", "GGTA", "CCTA", "TATA", "GCGC"]

GENES = {
    "U5": "ATCGATCG",
    "ADA": "GGGAAA",
    "FRAT1": "TTTCCC",
    "FXN": "AACCGG",
    "RNU6_269P": "GATTACA"
}

def read_html(path):
    file = open(path)
    content = file.read()
    file.close()
    return content


def complement(seq):
    result = ""
    for b in seq:
        if b == "A":
            result += "T"
        elif b == "T":
            result += "A"
        elif b == "C":
            result += "G"
        elif b == "G":
            result += "C"
    return result


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        params = urllib.parse.parse_qs(parsed.query)

        if path == "/":
            content = read_html("html/index.html")

        elif path == "/ping":
            content = read_html("html/ping.html")

        elif path == "/get":
            try:
                n = int(params.get("n", [0])[0])
                seq = SEQUENCES[n]
                content = read_html("html/get.html").replace("{{sequence}}", seq)
            except:
                content = read_html("html/error.html")

        elif path == "/gene":
            name = params.get("name", [""])[0]
            seq = GENES.get(name)

            if seq:
                content = read_html("html/gene.html").replace("{{gene}}", seq)
            else:
                content = read_html("html/error.html")

        elif path == "/operation":
            seq = params.get("seq", [""])[0]
            op = params.get("op", [""])[0]

            if op == "info":
                total = len(seq)
                result = f"""
Sequence: {seq}<br>
Total length: {total}<br>
A: {seq.count("A")}<br>
C: {seq.count("C")}<br>
G: {seq.count("G")}<br>
T: {seq.count("T")}
"""
            elif op == "comp":
                result = complement(seq)
            elif op == "rev":
                result = seq[::-1]
            else:
                result = "Invalid operation"

            content = read_html("html/operation.html").replace("{{result}}", result)

        else:
            content = read_html("html/error.html")

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(content.encode())


server = HTTPServer(("localhost", 8080), Handler)
print("Running on http://127.0.0.1:8080/")
server.serve_forever()