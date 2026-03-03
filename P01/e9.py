from Seq1 import Seq
from pathlib import Path

PRACTICE = 1
EXERCISE = 9

print(f"---- | Practice {PRACTICE} | Exercise {EXERCISE} |----")

FILENAME = Path("../S04/sequences/U5.txt")
file_contents = FILENAME.read_text()

seq = Seq()
seq.read_fasta(FILENAME)
seqs = [seq]

for i, s in enumerate(seqs):
    print(f"Sequence {i}: (Length: {s.length}) {s}")
    print(f"    Bases: {s.count()}")
    print(f"    Rev: {s.reverse()}")
    print(f"    Comp:{s.complement()}")