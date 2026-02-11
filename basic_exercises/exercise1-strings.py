dna = "ATGCGATCGATCGATCGATCGA"

def main():
    print("Length: ", len(dna))
    print("First 5:", dna[:5])
    print("Last 3:", dna[-3::])
    print("Lowercase:", dna.lower())
    print("ATC count:", dna.count('ATC'))
    print("RNA:", dna.replace("T", "U"))

main()