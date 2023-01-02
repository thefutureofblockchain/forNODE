import requests
import sys
import json
try:
    a = sys.argv[1]
    print(float(a))
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    o = response.json()
    for USD in o["bpi"]:
        amount = USD["rate_float"]
        print(f"${amount:,.4f}")

except requests.RequestException:
    pass
except ValueError:
    sys.exit("uh oh")

