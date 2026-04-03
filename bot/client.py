import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

def get_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    # CHANGED: added testnet=True to enable testnet mode
    client = Client(api_key, api_secret, testnet=True)

    # CHANGED: explicitly set futures testnet URL (required for futures orders)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client