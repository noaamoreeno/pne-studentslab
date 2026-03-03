from pathlib import Path

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

    def count_base(self,base):
        if self.strbases in ("NULL", "ERROR"):
            return 0
        return self.strbases.count(base)

    def count(self):
        bases = {"A": 0, "C": 0, "G": 0, "T": 0}
        if self.strbases in ("NULL", "ERROR"):
            return bases
        for base in self.strbases:
            bases[base] += 1
        return bases

    def reverse(self):
        if self.strbases == "NULL":
            return "NULL"
        elif self.strbases == "ERROR":
            return "ERROR"
        return str(self.strbases)[::-1]

    def complement(self):
        complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
        if self.strbases == "NULL":
            return "NULL"
        elif self.strbases == "ERROR":
            return "ERROR"
        return "".join([complement[b] for b in self.strbases])

    def read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        seq_lines = file_contents.split("\n")[1:]
        seq_str = "".join(seq_lines)
        self.__init__(seq_str)





    def __str__(self):
        return self.strbases
