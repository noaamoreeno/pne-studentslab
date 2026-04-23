from seq import Seq
import json
import http.client
import termcolor
from e2 import genes

gene_name = input("Enter gene name: ")

identifier = ''

for gene in genes:
    if gene['gene'] == gene_name:
        identifier = gene["identifier"]
        break

if identifier == '':
    print("Gene not found")
    exit()

SERVER = 'rest.ensembl.org'
ENDPOINT = f'/sequence/id/{identifier}'
PARAMS = '?content-type=application/json'

print(f"Write the gene name: {gene_name}")
print()
print(f"Server: {SERVER}")
print(f"URL: {SERVER}{ENDPOINT}{PARAMS}")

conn = http.client.HTTPSConnection(SERVER)

conn.request("GET", ENDPOINT + PARAMS)

response = conn.getresponse()
print(f"Response Received! {response.status} {response.reason}")

data = response.read().decode('utf-8')
result = json.loads(data)

sequence = result["seq"]
description = result["desc"]

seq = Seq(sequence)

print()
termcolor.cprint("Gene", "yellow", end=": ")
print(gene_name)

termcolor.cprint("Description", "yellow", end=": ")
print(description)

print("New sequence created!")

termcolor.cprint("Total length", "yellow", end=":")
print(seq.length())

for base, count in seq.base_count().items():
    termcolor.cprint(base, "blue", end=":")
    print(count)

termcolor.cprint("Most frequent base", "yellow", end=": ")
print(seq.most_frequent_base())