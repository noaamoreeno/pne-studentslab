from Seq0 import *

FOLDER = "../sequences/"
genes = ["U5", "ADA", "FRAT1", "FXN"]

print("-----| Exercise 5 |------")
for gene in genes:
    seq = seq_read_fasta(FOLDER + gene + ".txt")
    counts = seq_count(seq)
    print(f"Gene {gene}: {counts}")