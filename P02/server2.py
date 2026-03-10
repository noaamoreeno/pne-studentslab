import socket

IP = "10.8.41.140"
PORT = 8081

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.bind((IP, PORT))
ls.listen()

print(f"Waiting for connections at {IP}, {PORT}")

conn_number = 0

while True:

    cs, client_ip_port = ls.accept()

    conn_number += 1

    print(f"CONNECTION: {conn_number}. From the IP: {client_ip_port}")

    msg = cs.recv(2048).decode("utf-8")

    print(f"Message from client: {msg}")

    response = "\nHello from the teacher's server\n"

    cs.send(str.encode(response))

    cs.close()

    print(f"Waiting for connections at {IP}, {PORT}")