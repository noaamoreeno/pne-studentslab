import socket
import http.server
import http.client
import json
from urllib.parse import parse_qs, urlparse
from pathlib import Path

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

def ensembl_data(endpoint):
    try:
        conn = http.client.HTTPSConnection("rest.ensembl.org")
        conn.request("GET", endpoint + "?/content-type=application/json")
        response = conn.getresponse()

        if response.status == 200:
            data = response.read().decode("utf-8")
            return json.loads(data)

        else:
            return None

    except Exception as e:
        print(f"Error connecting to Ensembl: {e}")
        return None




