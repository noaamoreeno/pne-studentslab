
class Seq:
    """A class for representing"""
    def __init__(self,strbases):
        valid_bases = "ACGT"

        for base in strbases:
            if base not in valid_bases:
                self.strbases = "ERROR"
                print("incorrect sequence detected")
                return

        self.strbases = strbases
        print("New sequence created !")

    def __str__(self):
        return self.strbases


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")