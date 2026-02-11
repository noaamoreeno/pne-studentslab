#Write a program that prints:
# The total length of the string
# The first 5 characters
# The last 3 characters
# The string converted to lowercase
# How many times the substring "ATC" appears
# The string with all occurrences of "T" replaced by "U" (DNA to RNA transcription)

dna = "ATGCGATCGATCGATCGATCGA"

def main():
    print("Length: ", len(dna))
    print("First 5:", dna[:5])
    print("Last 3:", dna[-3::])
    print("Lowercase:", dna.lower())
    print("ATC count:", dna.count('ATC'))
    print("RNA:", dna.replace("T", "U"))

main()