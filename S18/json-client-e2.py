import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Conexión
conn = http.client.HTTPConnection(SERVER, PORT)

# Petición
try:
    conn.request("GET", "/listusers")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# Respuesta
r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")

# Leer datos
data = r1.read().decode("utf-8")

# Convertir JSON → Python
people = json.loads(data)

# 🔹 Número total de personas
print("Total people:", len(people))

# 🔹 Recorrer lista
for person in people:
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])

    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])

    phoneNumbers = person['phoneNumber']

    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    for i, num in enumerate(phoneNumbers):
        termcolor.cprint(f"  Phone {i}: ", 'blue')

        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])

        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])