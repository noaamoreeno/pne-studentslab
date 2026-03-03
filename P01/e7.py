from Seq1 import Seq

PRACTICE = 1
EXERCISE = 7

print(f"---- | Practice {PRACTICE} | Exercise {EXERCISE} |----")

seqs = [Seq(), Seq("ACTGA"), Seq("AXTGA")]

for i, s in enumerate(seqs):
    print(f"Sequence {i}: (Length: {s.length}) {s}")
    print(f"    Bases: {s.count()}")
    print(f"    Rev: {s.reverse()}")