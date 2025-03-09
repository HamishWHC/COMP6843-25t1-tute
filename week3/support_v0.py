from time import sleep

import requests

s = requests.session()
# Tell requests to use the certificate.
s.cert = "../HamishWHC.pem"

for i in range(1, 100000):
    r = s.get(f"https://support-v0.quoccacorp.com/raw/{i}/")

    if "HamishWHC" in r.text:
        print(r.text)

    if i % 25 == 0:
        print(i)

    sleep(0.1)
