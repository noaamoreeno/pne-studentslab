import socket

PORT = 8081
IP = "212.128.255.86"
while True:
    message = input("Enter your message: ")

    if message.lower() == "exit":
        print("Closing chat client...")
        break

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((IP, PORT))

    s.send(message.encode())

    s.close()