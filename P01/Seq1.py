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

    def __str__(self):
        return self.strbases
