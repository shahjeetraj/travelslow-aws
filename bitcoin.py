import requests
import json
import sys

if len(sys.argv) == 1:
    print("Missing command-line argument")
    sys.exit(1)
elif sys.argv[1].isalpha():
    print("Command-line argument is not a number")
    sys.exit(1)
else:
    qty = float(sys.argv[1])

try:
    x = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    json_str = json.dumps(x.json())
    resp = json.loads(json_str)
    rate = (resp['bpi']['USD']['rate_float'])
    amount = qty * rate
    print(f"${amount:,.4f}")

except requests.RequestException:
    print("Unable to fetch rates")
    sys.exit()