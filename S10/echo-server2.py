import socket
import termcolor

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.255.89"

# Create socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Avoid "Address already in use"
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind socket
ls.bind((IP, PORT))

# Listen
ls.listen()

print("The server is configured!")

conn_number = 0

while True:

    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

        conn_number += 1

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
