import requests

COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"

def get_price(coin_id: str) -> float:
    params = {
        "ids": coin_id,
        "vs_currencies": "usd"
    }

    response = requests.get(
        COINGECKO_API_URL,
        params=params,
        timeout=10
    )
    response.raise_for_status()

    data = response.json()
    return data[coin_id]["usd"]
