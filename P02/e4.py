from Client0 import Client
from P01.Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "10.8.41.140"
PORT = 8080

c = Client(IP, PORT)

print(c)

genes = {
    "U5": "../S04/sequences/U5.txt",
    "ADA": "../S04/sequences/ADA.txt",
    "FRAT1": "../S04/sequences/FRAT1.txt",
    "FXN": "../S04/sequences/FXN.txt",
    "RNU6_269P": "../S04/sequences/RNU6_269P.txt.txt"
}

genes_to_send = ["U5", "FRAT1", "ADA"]

for g in genes_to_send:

    print(f"Sending the {g} Gene to the server...")

    s = Seq()
    s.read_fasta(genes[g])

    sequence = str(s)

    response = c.talk(sequence)

    print(response)