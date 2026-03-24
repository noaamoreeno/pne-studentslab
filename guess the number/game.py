import socket
import random

class NumberGuesser:
    def __init__(self):
        self.secret_number = random.randint(1,100)
        self.attempts = []

    def guess(self,number):
        self.attempts.append(number)

        if number == self.secret_number:
            return f'You won after {len(self.attempts)} attempts'
        elif number > self.secret_number:
            return 'Lower'
        else:
            return 'Higher'

def start_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Server running on {host}:{port}...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        game = NumberGuesser()

        with conn:
            conn.sendall(b"Welcome! Guess a number between 1 and 100.\n")

            while not game.finished:
                data = conn.recv(1024)

                if data:
                    try:
                        guess = int(data.decode().strip())
                        response = game.guess(guess)
                    except ValueError:
                        response = "Please send a valid number."

                    conn.sendall((response + "\n").encode())
                else:
                    game.finished = True

        print(f"Connection closed: {addr}")

if __name__ == "__main__":
    start_server()





