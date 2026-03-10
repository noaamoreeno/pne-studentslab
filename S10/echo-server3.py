import socket
import termcolor

PORT = 8080
IP = "212.128.255.89"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))
ls.listen()

print("The server is configured!")

conn_number = 0
clients = []

while conn_number < 5:

    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

        conn_number += 1
        clients.append(client_ip_port)

        print(f"CONNECTION {conn_number}. Client IP,PORT: {client_ip_port}")

    except KeyboardInterrupt:

        print("Server stopped by the user")
        ls.close()
        exit()

    else:

        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()

        termcolor.cprint(f"Message received: {msg}", "green")

        response = f"ECHO: {msg}"
        cs.send(response.encode())

        cs.close()

print("The following clients has connected to the server:")

for i, client in enumerate(clients):
    print(f"Client {i}: {client}")

ls.close()