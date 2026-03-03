from pathlib import Path

FILENAME = "sequences/ADA.txt"

file_contents = Path(FILENAME).read_text()

sequence_list = (file_contents.split("\n"))[1::]
sequence = "".join(sequence_list)

print("Number of basis of ADA Human Gene:", len(sequence))