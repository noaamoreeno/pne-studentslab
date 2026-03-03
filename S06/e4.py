import termcolor

class Seq:
    def __init__(self, strbases):
        valid_bases = "ACGT"

        for base in strbases:
            if base not in valid_bases:
                self.strbases = "Error"
                print("Bases not valid")
                return

        self.strbases = strbases
        self.length = len(strbases)
        print("New sequence created !")

    def __str__(self):
        return self.strbases

def print_seqs(seq_list, color):
    for i, seq in enumerate(seq_list):
        print(f"Sequence{i}: (Length {seq.length}) {seq}")

def generate_seqs(pattern, number):
    seqs = []
    for i in range (1, number+1):
        new_pattern = pattern * i
        seqs.append(Seq(new_pattern))
    return seqs

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1, 'blue')

print()
print("List 2:")
print_seqs(seq_list2, 'yellow')

