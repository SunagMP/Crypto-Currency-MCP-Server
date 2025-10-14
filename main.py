# filename: coin_mcp.py
from fastmcp import FastMCP
import requests

# Initialize MCP
mcp = FastMCP(name="CoinGeckoMCP")

@mcp.tool
def get_crypto_price(coin: str, currency: str = "usd"):
    """
    Get current crypto price in USD or other currencies
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get(coin, {}).get(currency, "Coin or currency not found")
    return f"Error: {response.status_code}"

if __name__ == "__main__":
    mcp.run()