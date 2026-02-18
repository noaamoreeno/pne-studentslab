from pathlib import Path

def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    text = Path(filename).read_text()
    lines = text.split("\n")
    seq = "".join(lines[1:])
    return seq

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for base in d.keys():
        d[base] = seq.count(base)
    return d

def seq_reverse(seq, n):
    return seq[:n][::-1]

def seq_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join(complement[base] for base in seq)