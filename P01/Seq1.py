class Seq:
    def __init__(self, strbases=None):
        valid_bases = "ACGT"

        if strbases is None:
            self.strbases = "NULL"
            self.length = 0
            print("NULL sequence created")
            return

        for base in strbases:
            if base not in valid_bases:
                self.strbases = "ERROR"
                self.length = 0
                print("INVALID sequence!")
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