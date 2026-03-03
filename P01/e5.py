from Seq1 import Seq

from Seq1 import Seq

PRACTICE = 1
EXERCISE = 5

print(f"---- | Practice {PRACTICE} | Exercise {EXERCISE} |----")

seqs = [Seq(), Seq("ACTGA"), Seq("AXTGA")]

for i, s in enumerate(seqs):
    print(f"Sequence {i}: (Length: {s.length}) {s}")
    print(f"A: {s.count_base("A")}, C: {s.count_base("C")}, G: {s.count_base("G")}, T:{s.count_base("T")} ")
