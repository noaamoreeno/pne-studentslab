from pathlib import Path

FILENAME = "sequences/ADA.txt"
MAX_COORD = 44652852   # del header

file_contents = Path(FILENAME).read_text()

lines = file_contents.split("\n")

gene_seq = "".join(lines[1:])   # quitar cabecera

def analyze_exon(number, exon_seq):

    index = gene_seq.find(exon_seq)

    length = len(exon_seq)

    start = MAX_COORD - index
    end   = MAX_COORD - (index + length - 1)

    print(number, " | ", length, " | ", start, " | ", end)

exon1 = "GCTGGCCCCAGGGAAAGCCGAGCGGCCACCGAGCCGGCAGAGACCCACCGAGCGGCGGCGGAGGGAGCAGCGCCGGGGCGCACGAGGGCACCATGGCCCAGACGCCCGCCTTCGACAAGCCCAA"

exon2 = "GTGGAACTGCATGTCCACCTAGACGGATCCATCAAGCCTGAAACCATCTTATACTATGGCAG"

exon3 =

analyze_exon(1, exon1)
analyze_exon(2, exon2)
