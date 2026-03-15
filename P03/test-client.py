import socket

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def talk(self, message):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.sendall(message.encode())
        data = s.recv(65536)
        s.close()
        return data.decode().strip()


SERVER_IP = "127.0.0.1"
SERVER_PORT = 8080

client = Client(SERVER_IP, SERVER_PORT)

print("-----| Practice 3, Exercise 7 |------")
print(f"Connection to SERVER at {SERVER_IP}, PORT: {SERVER_PORT}")


print("* Testing PING...")
response = client.talk("PING")
print(response + "\n")

print("* Testing GET...")
get_responses = []
for i in range(5):
    response = client.talk(f"GET {i}")
    get_responses.append(response)
    print(f"GET {i}: {response}")
print("")

seq0 = get_responses[0]

print("* Testing INFO...")
response = client.talk(f"INFO {' '.join(seq0)}")
print(f"Sequence: {seq0}")

total = len(seq0)
A = seq0.count('A')
C = seq0.count('C')
G = seq0.count('G')
T = seq0.count('T')
print(f"Total length: {total}")
print(f"A: {A} ({A/total*100:.1f}%)")
print(f"C: {C} ({C/total*100:.1f}%)")
print(f"G: {G} ({G/total*100:.1f}%)")
print(f"T: {T} ({T/total*100:.1f}%)\n")

print("* Testing COMP...")
response = client.talk(f"COMP {' '.join(seq0)}")
print(f"COMP {seq0}")
print(response + "\n")

print("* Testing REV...")
response = client.talk(f"REV {' '.join(seq0)}")
print(f"REV {seq0}")
print(response + "\n")

print("* Testing GENE...")
for gene_name in ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]:
    response = client.talk(f"GENE {gene_name}")
    print(f"GENE {gene_name}")
    print(response[:200] + " [...]")

