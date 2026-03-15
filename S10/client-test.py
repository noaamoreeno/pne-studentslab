from Client0 import Client

IP = "212.128.255.89"
PORT = 8080

for i in range(5):

    message = f"Message {i}"

    print(f"To Server: {message}")

    client = Client(IP, PORT)

    response = client.talk(message)

    print(f"From Server: {response}")