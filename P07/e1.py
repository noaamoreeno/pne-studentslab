import json
import http.client

SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPSConnection(SERVER)

conn.request("GET", ENDPOINT + PARAMS)

response = conn.getresponse()
print(f"Response Received! {response.status} {response.reason}")

data = response.read().decode('utf-8')

response = json.loads(data)

print()
if response['ping'] == 1:
    print('PING OK! Database is running!')
else:
    print('Server is not running')