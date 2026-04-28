import json
import http.client
from e2 import genes
from seq import Seq
import termcolor

SERVER = "rest.ensembl.org"

for gene in genes:

    gene_name = gene["gene"]
    identifier = gene["identifier"]

    ENDPOINT = f"/sequence/id/{identifier}"
    PARAMS = "?content-type=application/json"

    conn = http.client.HTTPSConnection(SERVER)
    conn.request("GET", ENDPOINT + PARAMS)

    response = conn.getresponse()

    data = response.read().decode("utf-8")
    result = json.loads(data)

    sequence = result["seq"]
    description = result["desc"]

    seq = Seq(sequence)

    print("\n" + "="*40)
    termcolor.cprint("Gene", "yellow", end=": ")
    print(gene_name)
    termcolor.cprint("Description", "yellow", end=": ")
    print(description)

    termcolor.cprint("Total Length", "yellow", end=": ")
    print(seq.length())

    counts = seq.base_count()
    percen = seq.base_percentage()

    for base, count in counts.items():
        pct = percen[base]
        termcolor.cprint(base, "blue", end=": ")
        print(f"{count} ({pct:.2f}%)")

    print("Most frequent base:", seq.most_frequent_base())