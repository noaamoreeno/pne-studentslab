sequence = input("Introduce the sequence: ")
print("Length:", len(sequence))

def count_bases1():
    a = 0
    c = 0
    g = 0
    t = 0
    for base in sequence.upper():
        if base == "A":
            a += 1
        if base == "C":
            c += 1
        if base == "G":
            g += 1
        if base == "T":
            t += 1
    print("A:", a)
    print("C:", c)
    print("G:", g)
    print("T:", t)

#another method
def count_bases2():
    bases = {"A": 0, "C": 0, "G": 0, "T": 0}

    for base in sequence:
        if base in bases:
            bases[base]+=1

    print(bases)

def count_bases3():
    bases = {"A": 0, "C": 0, "G": 0, "T": 0}

    for base, count in bases.items():
        print(f"{base}:{count}")