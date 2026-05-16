import http.server
import http.client
import json
from urllib.parse import parse_qs, urlparse
from pathlib import Path
import jinja2 as j

PORT = 8080


# ── Jinja2 helper ────────────────────────────────
def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


# ── Ensembl API helper ────────────────────────────────────────────────────────
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


# ── Seq class ─────────────────────────────────────────────────────────────────
class Seq:
    BASES = ("A", "C", "G", "T")

    def __init__(self, sequence):
        self.sequence = sequence.upper()

    def __len__(self):
        return len(self.sequence)

    def count_bases(self):
        return {base: self.sequence.count(base) for base in self.BASES}

    def base_percentages(self):
        total = len(self.sequence)
        if total == 0:
            return {base: 0.0 for base in self.BASES}
        counts = self.count_bases()
        return {base: round(counts[base] / total * 100, 2) for base in self.BASES}


# ── Helper: resolve gene name → Ensembl stable ID ────────────────────────────
def gene_lookup_id(gene_name):
    data = ensembl_request(
        f"/lookup/symbol/homo_sapiens/{gene_name}?content-type=application/json"
    )
    if data and "id" in data:
        return data["id"]
    return None


# ── Request Handler ───────────────────────────────────────────────────────────
class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)
        path   = parsed.path
        params = parse_qs(parsed.query)
        want_json = params.get("json", [None])[0] == "1"

        if path == "/":
            # The main page never returns JSON, it always shows the HTML forms
            contents = read_html_file("index.html").render()
            self._send_html(contents)

        # ── /listSpecies ─────────────────────────────────────────────
        elif path == "/listSpecies":
            data = ensembl_request("/info/species?content-type=application/json")
            if data is None:
                self._send_error(want_json, "Could not reach Ensembl API.", 503)
                return

            species = [s["display_name"] for s in data["species"]]
            limit_param = params.get("limit", [None])[0]
            if limit_param:
                try:
                    species = species[:int(limit_param)]
                except ValueError:
                    self._send_error(want_json, "Limit must be a number.", 400)
                    return

            if want_json:
                self._send_json({"species": species})
            else:
                contents = read_html_file("listSpecies.html").render(
                    context={"species": species})
                self._send_html(contents)

        # ── /karyotype ───────────────────────────────────────────────
        elif path == "/karyotype":
            species = params.get("species", [None])[0]
            if not species:
                self._send_error(want_json, "Missing 'species' parameter.", 400)
                return

            data = ensembl_request(f"/info/assembly/{species}?content-type=application/json")
            if data is None:
                self._send_error(want_json, f"Species '{species}' not found.", 404)
                return

            karyotype = data.get("karyotype", [])

            if want_json:
                self._send_json({"species": species, "karyotype": karyotype})
            else:
                contents = read_html_file("karyotype.html").render(
                    context={"species": species, "karyotype": karyotype})
                self._send_html(contents)

        # ── /chromosomeLength ─────────────────────────────────────────
        elif path == "/chromosomeLength":
            species = params.get("species", [None])[0]
            chromo  = params.get("chromo",  [None])[0]
            if not species or not chromo:
                self._send_error(want_json, "Missing 'species' or 'chromo' parameter.", 400)
                return

            data = ensembl_request(f"/info/assembly/{species}?content-type=application/json")
            if data is None:
                self._send_error(want_json, f"Species '{species}' not found.", 404)
                return

            length = None
            for region in data.get("top_level_region", []):
                if region["name"] == chromo:
                    length = region["length"]
                    break

            if want_json:
                self._send_json({"species": species, "chromo": chromo, "length": length})
            else:
                contents = read_html_file("chromosomeLength.html").render(
                    context={"species": species, "chromo": chromo, "length": length})
                self._send_html(contents)

        # ── /geneLookup ───────────────────────────────────────────────
        elif path == "/geneLookup":
            gene = params.get("gene", [None])[0]
            if not gene:
                self._send_error(want_json, "Missing 'gene' parameter.", 400)
                return

            gene_id = gene_lookup_id(gene)
            if gene_id is None:
                self._send_error(want_json, f"Gene '{gene}' not found in Ensembl.", 404)
                return

            if want_json:
                self._send_json({"gene": gene, "gene_id": gene_id})
            else:
                contents = read_html_file("geneLookup.html").render(
                    context={"gene": gene, "gene_id": gene_id})
                self._send_html(contents)

        # ── /geneSeq ──────────────────────────────────────────────────
        elif path == "/geneSeq":
            gene = params.get("gene", [None])[0]
            if not gene:
                self._send_error(want_json, "Missing 'gene' parameter.", 400)
                return

            gene_id = gene_lookup_id(gene)
            if gene_id is None:
                self._send_error(want_json, f"Gene '{gene}' not found in Ensembl.", 404)
                return

            data = ensembl_request(f"/sequence/id/{gene_id}?content-type=application/json")
            if data is None or "seq" not in data:
                self._send_error(want_json, f"Could not retrieve sequence for '{gene}'.", 404)
                return

            sequence = data["seq"]

            if want_json:
                self._send_json({"gene": gene, "gene_id": gene_id,
                                 "sequence": sequence, "length": len(sequence)})
            else:
                contents = read_html_file("geneSeq.html").render(
                    context={"gene": gene, "gene_id": gene_id,
                             "sequence": sequence, "length": len(sequence)})
                self._send_html(contents)

        # ── /geneInfo ─────────────────────────────────────────────────
        elif path == "/geneInfo":
            gene = params.get("gene", [None])[0]
            if not gene:
                self._send_error(want_json, "Missing 'gene' parameter.", 400)
                return

            gene_id = gene_lookup_id(gene)
            if gene_id is None:
                self._send_error(want_json, f"Gene '{gene}' not found in Ensembl.", 404)
                return

            data = ensembl_request(f"/lookup/id/{gene_id}?content-type=application/json")
            if data is None:
                self._send_error(want_json, f"Could not retrieve info for '{gene}'.", 404)
                return

            start     = data.get("start", 0)
            end       = data.get("end",   0)
            length    = end - start + 1 if isinstance(start, int) and isinstance(end, int) else 0
            gene_name = data.get("display_name", gene)
            chromo    = data.get("seq_region_name", "N/A")

            if want_json:
                self._send_json({"gene": gene, "gene_id": gene_id,
                                 "gene_name": gene_name, "chromo": chromo,
                                 "start": start, "end": end, "length": length})
            else:
                contents = read_html_file("geneInfo.html").render(
                    context={"gene": gene, "gene_id": gene_id,
                             "gene_name": gene_name, "chromo": chromo,
                             "start": start, "end": end, "length": length})
                self._send_html(contents)

        # ── /geneCalc ─────────────────────────────────────────────────
        elif path == "/geneCalc":
            gene = params.get("gene", [None])[0]
            if not gene:
                self._send_error(want_json, "Missing 'gene' parameter.", 400)
                return

            gene_id = gene_lookup_id(gene)
            if gene_id is None:
                self._send_error(want_json, f"Gene '{gene}' not found in Ensembl.", 404)
                return

            data = ensembl_request(f"/sequence/id/{gene_id}?content-type=application/json")
            if data is None or "seq" not in data:
                self._send_error(want_json, f"Could not retrieve sequence for '{gene}'.", 404)
                return

            seq = Seq(data["seq"])

            if want_json:
                self._send_json({"gene": gene, "gene_id": gene_id,
                                 "length": len(seq),
                                 "percentages": seq.base_percentages()})
            else:
                contents = read_html_file("geneCalc.html").render(
                    context={"gene": gene, "gene_id": gene_id,
                             "length": len(seq),
                             "percentages": seq.base_percentages()})
                self._send_html(contents)

        # ── /geneList ─────────────────────────────────────────────────
        elif path == "/geneList":
            chromo = params.get("chromo", [None])[0]
            start  = params.get("start",  [None])[0]
            end    = params.get("end",    [None])[0]

            if not chromo or not start or not end:
                self._send_error(want_json,
                                 "Missing 'chromo', 'start', or 'end' parameter.", 400)
                return

            try:
                start_int = int(start)
                end_int   = int(end)
            except ValueError:
                self._send_error(want_json, "'start' and 'end' must be integers.", 400)
                return

            data = ensembl_request(
                f"/overlap/region/human/{chromo}:{start_int}-{end_int}"
                f"?feature=gene;content-type=application/json"
            )
            if data is None:
                self._send_error(want_json,
                                 f"Could not retrieve genes for region {chromo}:{start}-{end}.",
                                 404)
                return

            genes = sorted(set(
                g.get("external_name") or g.get("gene_id", "unknown") for g in data
            ))

            if want_json:
                self._send_json({"chromo": chromo, "start": start_int,
                                 "end": end_int, "genes": genes})
            else:
                contents = read_html_file("geneList.html").render(
                    context={"chromo": chromo, "start": start_int,
                             "end": end_int, "genes": genes})
                self._send_html(contents)

        # ── 404 ───────────────────────────────────────────────────────
        else:
            self._send_error(want_json, f"Endpoint '{path}' not found.", 404)

    # ── Helper: send HTML response ────────────────────────────────────
    def _send_html(self, content, status=200):
        encoded = content.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    # ── Helper: send JSON response ────────────────────────────────────
    def _send_json(self, data, status=200):
        encoded = json.dumps(data, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    # ── Helper: send error in HTML or JSON depending on what client wants ──
    def _send_error(self, want_json, message, status):
        if want_json:
            self._send_json({"error": message}, status)
        else:
            contents = read_html_file("error.html").render(
                context={"message": message})
            self._send_html(contents, status)

    def log_message(self, fmt, *args):
        print(f"[{self.address_string()}] {fmt % args}")

http.server.HTTPServer.allow_reuse_address = True

with http.server.HTTPServer(("", PORT), Handler) as httpd:
    print(f"Serving on http://localhost:{PORT}")
    httpd.serve_forever()



