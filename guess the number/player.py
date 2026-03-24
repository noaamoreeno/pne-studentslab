import socket

def start_client(host='127.0.0.1', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    finished = False

    try:

        data = client_socket.recv(1024)
        print(data.decode())

        while not finished:
            user_input = input("Enter your guess: ")

            client_socket.sendall((user_input + "\n").encode())

            response = client_socket.recv(1024).decode().strip()

            if response.startswith("Higher"):
                print("\033[94m" + response + "\033[0m")  # Blue
            elif response.startswith("Lower"):
                print("\033[91m" + response + "\033[0m")  # Red
            elif response.startswith("You won"):
                print("\033[92m" + response + "\033[0m")  # Green
                finished = True
            else:
                print(response)

    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    start_client()