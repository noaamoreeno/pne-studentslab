from Seq0 import *

FOLDER = "..S04/sequences/"
FILENAME = "U5.txt"

print("-----| Exercise 7 |------")
seq = seq_read_fasta(FOLDER + FILENAME)
fragment = seq[:20]
comp = seq_complement(fragment)
print("Gene U5:")
print("Frag:", fragment)
print("Comp:", comp)