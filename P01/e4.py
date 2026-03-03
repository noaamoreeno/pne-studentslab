from Seq1 import Seq

PRACTICE = 1
EXERCISE = 4

print(f"---- | Practice {PRACTICE} | Exercise {EXERCISE} |----")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("ACTXXGA")

print(f"Sequence 1: (Length: {s1.length}) {s1}")
print(f"Sequence 2: (Length: {s2.length}) {s2}")
print(f"Sequence 3: (Length: {s3.length}) {s3}")