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

def print_seqs(seq_list):
    for i, seq in enumerate(seq_list):
        print(f"Sequence{i}: (Length {seq.length}) {seq}")

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)