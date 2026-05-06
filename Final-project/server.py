import http.server
import http.client
import json
from urllib.parse import parse_qs, urlparse

PORT = 8080

def ensembl_request(endpoint):
    try:
        conn = http.client.HTTPSConnection("rest.ensembl.org")
        conn.request("GET", endpoint, headers={"Content-Type": "application/json"})
        response = conn.getresponse()
        if response.status == 200:
            return json.loads(response.read().decode("utf-8"))
        return None
    except Exception as e:
        print(f"Ensembl error: {e}")
        return None

# ── HTML page builder ───────────────────────────────────────────────────────
def build_page(title, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <style>
    body {{ background-color: #9b59b6; font-family: serif; padding: 20px; }}
    h1   {{ font-size: 36px; font-weight: bold; }}
    ul   {{ font-size: 18px; }}
    p    {{ font-size: 18px; }}
    a    {{ color: #2c0040; font-size: 16px; }}
  </style>
</head>
<body>
{body}
<br><a href="/">&#8592; Back to main page</a>
</body>
</html>"""

# ── Error page helper ───────────────────────────────────────────────────────
def error_page(msg):
    return build_page("Error", f"<h1>Error</h1><p>{msg}</p>")

# ── Main HTML page (served at /) ────────────────────────────────────────────
MAIN_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Genome Browser</title>
  <style>
    body {
      background-color: #9b59b6;
      font-family: serif;
      padding: 20px;
    }
    h1 { font-size: 42px; font-weight: bold; color: black; }
    h2 { font-size: 32px; font-weight: bold; color: black; }
    h3 { font-size: 24px; color: black; }
    form {
      font-size: 18px;
      color: black;
      margin-bottom: 30px;
    }
    input[type="text"] {
      font-size: 16px;
      border: 2px solid purple;
      border-radius: 4px;
      padding: 4px;
    }
    input[type="submit"] {
      font-size: 18px;
      margin-top: 10px;
      background-color: plum;
      color: black;
      cursor: pointer;
      border: 2px solid purple;
      border-radius: 4px;
    }
    input[type="submit"]:hover { background-color: violet; }
  </style>
</head>
<body>
  <h1>Browsing Human and Vertebrates genome</h1>
  <h2>BASIC Level Services</h2>

  <!-- Form 1: sends GET /listSpecies?limit=... -->
  <h3>1) List of species in the genome database</h3>
  <form action="/listSpecies" method="get">
    Limit : <input type="text" name="limit">
    <br>
    <input type="submit" value="Send">
  </form>

  <!-- Form 2: sends GET /karyotype?species=... -->
  <h3>2) Information about the karyotype</h3>
  <form action="/karyotype" method="get">
    Select the species : <input type="text" name="species">
    <br>
    <input type="submit" value="Send">
  </form>

  <!-- Form 3: sends GET /chromosomeLength?species=...&chromo=... -->
  <h3>3) Chromosome Length</h3>
  <form action="/chromosomeLength" method="get">
    Select the species : <input type="text" name="species">
    <br><br>
    Select a chromosome : <input type="text" name="chromo">
    <br>
    <input type="submit" value="Send">
  </form>
</body>
</html>"""

# ── Request Handler ─────────────────────────────────────────────────────────
class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)
        path   = parsed.path
        params = parse_qs(parsed.query)

        # ── main page ───────────────────────────────────────────────
        if path == "/":
            self._send_html(MAIN_PAGE)

        # ── /listSpecies ────────────────────────────────────────────────
        elif path == "/listSpecies":
            data = ensembl_request("/info/species?content-type=application/json")
            if data is None:
                self._send_html(error_page("Could not reach Ensembl API."), 503)
                return

            species = [s["display_name"] for s in data["species"]]

            limit_param = params.get("limit", [None])[0]
            if limit_param:
                try:
                    species = species[:int(limit_param)]
                except ValueError:
                    self._send_html(error_page("Limit must be a number."), 400)
                    return

            items = "".join(f"<li>{s}</li>" for s in species)
            body  = f"<h1>Species list ({len(species)} shown)</h1><ul>{items}</ul>"
            self._send_html(build_page("Species List", body))

        # ── /karyotype ──────────────────────────────────────────────────
        elif path == "/karyotype":
            species = params.get("species", [None])[0]
            if not species:
                self._send_html(error_page("Missing 'species' parameter."), 400)
                return

            data = ensembl_request(f"/info/assembly/{species}?content-type=application/json")
            if data is None:
                self._send_html(error_page(f"Species '{species}' not found."), 404)
                return

            karyotype = data.get("karyotype", [])
            if karyotype:
                items = "".join(f"<li>{c}</li>" for c in karyotype)
                body  = f"<h1>Karyotype of {species}</h1><ul>{items}</ul>"
            else:
                body  = f"<h1>Karyotype of {species}</h1><p>No karyotype data available.</p>"
            self._send_html(build_page("Karyotype", body))

        # ── /chromosomeLength ───────────────────────────────────────────
        elif path == "/chromosomeLength":
            species = params.get("species", [None])[0]
            chromo  = params.get("chromo",  [None])[0]
            if not species or not chromo:
                self._send_html(error_page("Missing 'species' or 'chromo' parameter."), 400)
                return

            data = ensembl_request(f"/info/assembly/{species}?content-type=application/json")
            if data is None:
                self._send_html(error_page(f"Species '{species}' not found."), 404)
                return

            length = None
            for region in data.get("top_level_region", []):
                if region["name"] == chromo:
                    length = region["length"]
                    break  # Found it, stop looping

            if length is None:
                body = f"<h1>Chromosome {chromo} – {species}</h1><p>Chromosome not found.</p>"
            else:
                # {:,} adds thousands separators: 90772031 → 90,772,031
                body = f"<h1>Chromosome {chromo} – {species}</h1><p>Length: <strong>{length:,}</strong> bp</p>"
            self._send_html(build_page("Chromosome Length", body))

        else:
            self._send_html(error_page(f"Endpoint '{path}' not found."), 404)

    # ── Helper: encode and send an HTML string ──────────────────────────
    def _send_html(self, content, status=200):

        encoded = content.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    # ── Helper: cleaner terminal logs ───────────────────────────────────
    def log_message(self, fmt, *args):
        print(f"[{self.address_string()}] {fmt % args}")

# ── Start the server ────────────────────────────────────────────────────────
http.server.HTTPServer.allow_reuse_address = True  # Avoids "address in use" error on restart

with http.server.HTTPServer(("", PORT), Handler) as httpd:
    print(f"Serving on http://localhost:{PORT}")
    httpd.serve_forever()


