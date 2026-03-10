from Client0 import Client
from P00.Seq0 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "10.8.41.140"

PORT1 = 8080
PORT2 = 8081

c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)

print(c1)
print(c2)

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

for i in range(10):

    fragment = gene[i*10:(i+1)*10]

    print(f"Fragment {i+1}: {fragment}")

    if (i+1) % 2 != 0:
        c1.talk(fragment)
    else:
        c2.talk(fragment)