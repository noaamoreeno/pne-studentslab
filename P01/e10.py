from Seq1 import Seq
from pathlib import Path

PRACTICE = 1
EXERCISE = 10

print(f"---- | Practice {PRACTICE} | Exercise {EXERCISE} |----")

genes = {  "U5": "../S04/sequences/U5.txt",
    "ADA": "../S04/sequences/ADA.txt",
    "FRAT1": "../S04/sequences/FRAT1.txt",
    "FXN": "../S04/sequences/FXN.txt",
    "RNU6_269P": "../S04/sequences/RNU6_269P.txt.txt"
}

for gene_name, file_path in genes.items():
    seq = Seq()
    seq.read_fasta(Path(file_path))

    base_counts = seq.count()
    most_common = None
    highest_count = -1
    for base, count in base_counts.items():
        if count > highest_count:
            highest_count = count
            most_common = base

    print(f"Gene {gene_name}: Most frequent base {most_common}")
