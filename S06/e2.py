class Seq:
    """A class for representing DNA sequences"""
    def __init__(self, strbases):
        valid_bases = "ACGT"

        for base in strbases:
            if base not in valid_bases:
                raise ValueError("Incorrect sequence detected")
        self.strbases = strbases
    def __str__(self):
        return self.strbases

def print_seqs(seq_list):
    for index, seq in enumerate(seq_list):
        print(f"Sequence {index}: (Length: {len(seq.strbases)}) {seq}")


# Example
seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)