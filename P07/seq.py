class Seq:
    def __init__(self, sequence):
        self.sequence = sequence.upper()

    def length(self):
        return len(self.sequence)

    def info(self):
        return f"Length: {len(self.sequence)}"

    def base_count(self):
        return {
            "A": self.sequence.count("A"),
            "T": self.sequence.count("T"),
            "C": self.sequence.count("C"),
            "G": self.sequence.count("G")
        }

    def base_percentage(self):
        length = self.length()
        counts = self.base_count()
        return {base: (count / length) * 100 for base, count in counts.items()}

    def most_frequent_base(self):
        counts = self.base_count()
        return max(counts, key=counts.get)

    def reverse(self):
        return self.sequence[::-1]