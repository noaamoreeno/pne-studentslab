import json
import http.client
from e2 import genes
import termcolor

identifier = ''
for gene in genes:
    if gene['gene'] == 'MIR633':
        identifier = gene['identifier']
        break

SERVER = 'rest.ensembl.org'
ENDPOINT = f'/sequence/id/{identifier}'
PARAMS = '?content-type=application/json'

print()
print(f"Server: {SERVER}")
print(f"URL: {SERVER}{ENDPOINT}{PARAMS}")

conn = http.client.HTTPSConnection(SERVER)

conn.request("GET", ENDPOINT + PARAMS)

response = conn.getresponse()
print(f"Response Received! {response.status} {response.reason}")

data = response.read().decode('utf-8')
result = json.loads(data)


print()
termcolor.cprint("Gene", "Yellow", end=": " )
print("MIR633")

termcolor.cprint(f"Description", "Yellow", end= ": ")
print(result["desc"])

termcolor.cprint("Bases", "Yellow", end=": ")
print(result["seq"])



