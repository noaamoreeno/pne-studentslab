from pathlib import Path

FILENAME = "sequences/U5.txt"

file_contents = Path(FILENAME).read_text()

body = (file_contents.split("\n"))[1::]
print("Body of the U5.txt file", "\n", "\n".join(body))