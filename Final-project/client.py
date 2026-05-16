import http.client
import json

SERVER = "localhost"
PORT   = 8080

def server_request(endpoint):
    try:
        conn = http.client.HTTPConnection(SERVER, PORT)
        if "?" in endpoint:
            url = endpoint + "&json=1"
        else:
            url = endpoint + "?json=1"

        conn.request("GET", url)
        response = conn.getresponse()
        data = json.loads(response.read().decode("utf-8"))
        return data

    except Exception as e:
        print(f"Error connecting to server: {e}")
        print("Make sure the server is running on localhost:8080")
        return None

def separator(title):
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)

separator("TEST 1: List of species (limit 5)")

data = server_request("/listSpecies?limit=5")

if data:
    if "error" in data:
        print(f"  ERROR: {data['error']}")
    else:
        print(f"  Total species shown: {len(data['species'])}")
        for species in data["species"]:
            print(f"    - {species}")

separator("TEST 2: Karyotype of human")

data = server_request("/karyotype?species=human")

if data:
    if "error" in data:
        print(f"  ERROR: {data['error']}")
    else:
        print(f"  Species: {data['species']}")
        print(f"  Chromosomes: {data['karyotype']}")


separator("TEST 3: Length of human chromosome 1")

data = server_request("/chromosomeLength?species=human&chromo=1")

if data:
    if "error" in data:
        print(f"  ERROR: {data['error']}")
    else:
        print(f"  Species:    {data['species']}")
        print(f"  Chromosome: {data['chromo']}")
        print(f"  Length:     {data['length']:,} bp")

separator("TEST 4: Gene Lookup for FRAT1")

data = server_request("/geneLookup?gene=FRAT1")

if data:
    if "error" in data:
        print(f"  ERROR: {data['error']}")
    else:
        print(f"  Gene name:  {data['gene']}")
        print(f"  Ensembl ID: {data['gene_id']}")


separator("TEST 5: Gene Information for FRAT1")

data = server_request("/geneInfo?gene=FRAT1")

if data:
    if "error" in data:
        print(f"  ERROR: {data['error']}")
    else:
        print(f"  Gene name:  {data['gene_name']}")
        print(f"  Ensembl ID: {data['gene_id']}")
        print(f"  Chromosome: {data['chromo']}")
        print(f"  Start:      {data['start']:,}")
        print(f"  End:        {data['end']:,}")
        print(f"  Length:     {data['length']:,} bp")


separator("TEST 6: Gene Calculations for FRAT1")

data = server_request("/geneCalc?gene=FRAT1")

if data:
    if "error" in data:
        print(f"  ERROR: {data['error']}")
    else:
        print(f"  Gene:   {data['gene']} ({data['gene_id']})")
        print(f"  Length: {data['length']:,} bp")
        print(f"  Base percentages:")
        for base, pct in data["percentages"].items():
            print(f"    {base}: {pct:.2f}%")

separator("TEST 7: Gene Sequence for FRAT1")

data = server_request("/geneSeq?gene=FRAT1")

if data:
    if "error" in data:
        print(f"  ERROR: {data['error']}")
    else:
        print(f"  Gene:     {data['gene']} ({data['gene_id']})")
        print(f"  Length:   {data['length']:,} bp")
        print(f"  Sequence: {data['sequence'][:60]}...")


separator("TEST 8: Gene List in chromosome 9, region 22125500-22136000")

data = server_request("/geneList?chromo=9&start=22125500&end=22136000")

if data:
    if "error" in data:
        print(f"  ERROR: {data['error']}")
    else:
        print(f"  Chromosome: {data['chromo']}")
        print(f"  Region:     {data['start']:,} – {data['end']:,}")
        print(f"  Genes found ({len(data['genes'])}):")
        for gene in data["genes"]:
            print(f"    - {gene}")

separator("TEST 9: Error handling — gene that does not exist")

data = server_request("/geneInfo?gene=THISDOESNOTEXIST")

if data:
    if "error" in data:
        print(f"  Server correctly returned an error:")
        print(f"  ERROR: {data['error']}")
    else:
        print(f"  Unexpected response: {data}")


print("\n" + "=" * 60)
print("  All tests finished")
print("=" * 60 + "\n")