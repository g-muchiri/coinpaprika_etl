import requests

def extract_coin_data ():
    url = "https://api.coinpaprika.com/v1/tickers/{coin_id}?quotes=USD"

    coins_id= {'btc-bitcoin','eth-ethereum','trx-tron'}

    coin_data = []


    ##url.format here is used to treat placeholders in url
    for coin in coins_id:
        response = requests.get(url.format(coin_id = coin))
        response.raise_for_status()
        coin_data.append(response.json())

    return coin_data
