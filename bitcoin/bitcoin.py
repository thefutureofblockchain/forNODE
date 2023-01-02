import requests
import sys
import json
try:
    a = sys.argv[1]
    a = float(a)
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    #print(json.dumps(response.json(), indent=2))
    o = response.json()
    ab = o["bpi"]
    b = ab["USD"]
    rate = b["rate_float"]
    rate = float(rate)
    ba = a*rate
    print(f"${ba:,.4f}")
except requests.RequestException:
    pass
except ValueError:
    sys.exit("uh oh")

