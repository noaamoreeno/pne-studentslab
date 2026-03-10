from Client0 import Client
from P01.Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

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

s = Seq()
s.read_fasta(genes["FRAT1"])

gene = str(s)

print(f"Gene FRAT1: {gene[:60]}...")

for i in range(5):

    fragment = gene[i*10:(i+1)*10]

    print(f"Fragment {i+1}: {fragment}")

    c.talk(fragment)