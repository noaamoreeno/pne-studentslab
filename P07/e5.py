import json
import http.client
from e2 import genes
from seq import Seq

SERVER = "rest.ensembl.org"

for gene in genes:

    gene_name = gene["gene"]
    identifier = gene["identifier"]

    ENDPOINT = f"/sequence/id/{identifier}"
    PARAMS = "?content-type=application/json"

    conn = http.client.HTTPSConnection(SERVER)
    conn.request("GET", ENDPOINT + PARAMS)

    response = conn.getresponse()

    if response.status != 200:
        print(f"Error with {gene_name}: {response.status}")
        continue

    data = response.read().decode()
    result = json.loads(data)

    sequence = result["seq"]
    description = result["desc"]

    seq = Seq(sequence)

    print("\n" + "="*40)
    print("Gene:", gene_name)
    print("Identifier:", identifier)
    print("Description:", description)

    print("Length:", seq.length())

    print("Base counts:")
    for base, count in seq.base_count().items():
        print(base, ":", count)

    print("Base percentages:")
    for base, pct in seq.base_percentage().items():
        print(base, ":", round(pct, 2), "%")

    print("Most frequent base:", seq.most_frequent_base())