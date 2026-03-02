from Client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "10.77.135.166"
PORT = 8080

c = Client(IP, PORT)
c.ping()
print(f"Configured IP: {c.ip}, PORT: {c.port}")