from Seq0 import *

FOLDER = "../sequences/"
FILENAME = "U5.txt"

print("DNA file:", FILENAME)
seq = seq_read_fasta(FOLDER + FILENAME)
print("The first 20 bases are: ")
print(seq[:20])
