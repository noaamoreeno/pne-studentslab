lines = ["AGTACACTGGT", "ACCAGTGTACT", "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"]

def count_bases():
    for sequence in lines:
        info = {"Length": len(sequence), "A": 0, "C": 0, "G": 0, "T": 0}

        for base in sequence:
            if base in info:
                info[base] += 1

        print("Sequence:", sequence)
        for base, count in info.items():
            print(f'{base}:{count}')


count_bases()
