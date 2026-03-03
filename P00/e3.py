from Seq0 import *

FOLDER = "../sequences/"
genes = ["U5", "ADA", "FRAT1", "FXN"]

print("-----| Exercise 3 |------")
for gene in genes:
    seq = seq_read_fasta(FOLDER + gene + ".txt")
    print(f"Gene {gene} -> Length: {seq_len(seq)}")