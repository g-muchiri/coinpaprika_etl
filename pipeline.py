import requests

url = "https://api.coinpaprika.com/v1/tickers?quotes=USD"

response = requests.get(url)

print(response.text)