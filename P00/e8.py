from Seq0 import *

FOLDER = "../sequences/"
genes = ["U5", "ADA", "FRAT1", "FXN"]

print("-----| Exercise 8 |------")
for gene in genes:
    seq = seq_read_fasta(FOLDER + gene + ".txt")
    counts = seq_count(seq)
    most_freq_base = max(counts, key=counts.get)
    print(f"Gene {gene}: Most frequent Base: {most_freq_base}")