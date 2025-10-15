import requests

KEY = "c76345e254b549a7be938a851515f716"
URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

PARAMS = {"symbol": "SOL"}

HEADERS = {"X-CMC_PRO_API_KEY": KEY, "Accepts": "application/json"}

response = requests.get(URL, headers=HEADERS, params=PARAMS)
data = response.json()

print("SOL price (USD):", data['data']['SOL']['quote']['USD']['price'])
# print(data)
