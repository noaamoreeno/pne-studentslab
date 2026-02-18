from Seq0 import *

FOLDER = "../sequences/"
FILENAME = "U5.txt"

print("------| Exercise 6 |------")
seq = seq_read_fasta(FOLDER + FILENAME)
fragment = seq[:20]
print("Gene U5")
print("Fragment: ", fragment)
print("Reverse: ", seq_reverse(fragment, len(fragment)))