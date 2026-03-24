import socket

class Seq:
    def __init__(self, sequence):
        self.sequence = sequence

    def info(self):
        length = len(self.sequence)
        total = sum(self.sequence)
        maximum = max(self.sequence)
        return f"Length: {length}, Total: {total}, Max: {maximum}"

    def complement(self):
        if not self.sequence:
            return []
        maximum = max(self.sequence)
        return [maximum - x for x in self.sequence]

    def reverse(self):
        return self.sequence[::-1]

    def read_gene_file(self, filepath):
        with open(filepath, "r") as f:
            content = f.read.strip()
        sequence_list = file_contents.split("\n")[1:]
        return list("".join(sequence_list))

IP = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(1)

conn, addr = server.accept()
print("Connected by", addr)

sequences = [[1, 2, 3], [10, 20, 30, 40], [5, 4, 3, 2, 1], [7, 14, 21], [0, 0, 0, 0]]
genes = {
    "U5": "../S04/sequences/U5.txt",
    "ADA": "../S04/sequences/ADA.txt",
    "FRAT1": "../S04/sequences/FRAT1.txt",
    "FXN": "../S04/sequences/FXN.txt",
    "RNU6_269P": "../S04/sequences/RNU6_269P.txt"
}

flag = True
while flag:
    data = conn.recv(1024)
    if not data:
        flag = False

    message = data.decode().strip()

    if message == "PING":
        print("PING command !")
        response = "OK! \n"

        conn.sendall(response.encode())

    elif message.startswith("GET"):
        number = int(message.split()[1])
        response = str(sequences[number]) + "\n"
        print(f"GET command for sequence {number}: {response.strip()}")
        conn.sendall(response.encode())

    elif message.startswith("INFO"):
        parts = message.split()[1:]
        seq_numbers = [int(x) for x in parts]
        seq_obj = Seq(seq_numbers)
        info_res = seq_obj.info() + "\n"
        print(f"INFO command for sequence {seq_numbers}: {info_res.strip()}")
        conn.sendall(info_res.encode())

    elif message.startswith("COMP"):
        parts = message.split()[1:]
        seq_numbers = [int(x) for x in parts]
        seq_obj = Seq(seq_numbers)
        comp_res = str(seq_obj.complement())
        print(f"COMP command for sequence {seq_numbers}: {comp_res.strip()}")
        conn.sendall(comp_res.encode())

    elif message.startswith("REV"):
        parts = message.split()[1:]
        seq_numbers = [int(x) for x in parts]
        seq_obj = Seq(seq_numbers)
        rev_res = str(seq_obj.reverse()) + "\n"
        print(f"REV command for sequence {seq_numbers}: {rev_res.strip()}")
        conn.sendall(rev_res.encode())

    elif message.startswith("GENE"):
        gene_name = message.split()[1]
        if gene_name in genes:
            seq_obj = Seq([])
            gene_sequence = seq_obj.read_gene_file(genes[gene_name])
            response = str(gene_sequence) + "\n"
        else:
            response = "Error: gene not found"
        print(f"GENE command for sequence {gene_name}: {response.strip()}")
        conn.sendall(response.encode())

conn.close()
