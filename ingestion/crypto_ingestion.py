import json

import requests

ping_resp = requests.get("https://api.coingecko.com/api/v3/ping")

if ping_resp:
    ping_json = json.loads(ping_resp.content)
    print(ping_json)
