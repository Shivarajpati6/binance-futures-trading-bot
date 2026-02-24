import os
from dotenv import load_dotenv
from binance.client import Client

# Load environment variables
load_dotenv()

# Get API keys from .env
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

print("API KEY LOADED:", API_KEY is not None)
print("SECRET LOADED:", API_SECRET is not None)

# Create Futures Testnet client
client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"


def place_order(symbol, side, order_type, quantity, price=None):
    try:
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        order = client.futures_create_order(**params)
        return order

    except Exception as e:
        return {"error": str(e)}