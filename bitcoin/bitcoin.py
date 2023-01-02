import requests
import sys
import json
try:
    a = sys.argv[1]
    print(float(a))
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    o = response.json()
    print(o, indent = 2 )
    '''for result in o["bpi"]:
        amount =
        print(f"${amount:,.4f}")'''

except requests.RequestException:
    pass
except ValueError:
    sys.exit("uh oh")

