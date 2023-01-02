import requests
import sys
try:
    a = sys.argv[1]
    print(float(a))

except requests.RequestException:
    pass
except ValueError:
    sys.exit("uh oh")

