import requests
import sys
try:
    a = sys.argv[1]
    print(float(a))
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    print(response.json())

except requests.RequestException:
    pass
except ValueError:
    sys.exit("uh oh")

