import socket

IP = "212.128.255.64"
PORT = 8081

while True:
    message = input("Write a message (type 'exit' to quit): ")

    if message.lower() == "exit":
        print("Closing client...")
        break

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((IP, PORT))

    s.send(message.encode())

    response = s.recv(2048).decode("utf-8")
    print("Server says:", response)

    s.close()