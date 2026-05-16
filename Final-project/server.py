import http.server
import http.client
import json
from urllib.parse import parse_qs, urlparse
from pathlib import Path

PORT = 8080

    try:
        conn = http.client.HTTPSConnection("rest.ensembl.org")
        response = conn.getresponse()
        if response.status == 200:
        return None
    except Exception as e:
    return None




