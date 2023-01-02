import requests
import sys
import json
try:
    a = sys.argv[1]
    print(float(a))
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    print(json.dumps(response.json(), indent=2))

except requests.RequestException:
    pass
except ValueError:
    sys.exit("uh oh")

