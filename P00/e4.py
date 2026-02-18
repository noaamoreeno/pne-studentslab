from Seq0 import *

FOLDER = "../sequences/"
genes = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "T", "G"]

print("-----| Exercise 4 |------")
for gene in genes:
    seq = seq_read_fasta(FOLDER + gene + ".txt")
    print(f"\nGene {gene}:")
    for base in bases:
        print(f"  {base}: {seq_count_base(seq, base)}")