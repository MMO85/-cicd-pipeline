import os
from typing import Any

import dotenv
import requests

dotenv.load_dotenv()

_BASE_URL = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"

COINMARKETCAP_API_KEY = os.getenv("COINMARKETCAP_API_KEY", "")
COINMARKETCAP_SYMBOLS = os.getenv("COINMARKETCAP_SYMBOLS", "BTC")

UPDATE_FREQ_SEC = int(os.getenv("UPDATE_FREQ_SEC", 60))


def get_response() -> requests.Response:
    try:
        response = requests.get(
            url=_BASE_URL,
            headers={
                "Accept": "application/json",
                "X-CMC_PRO_API_KEY": COINMARKETCAP_API_KEY,
            },
            params={"symbol": COINMARKETCAP_SYMBOLS},
            timeout=10,
        )

        response.raise_for_status()
        return response

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"API request failed: {e}") from e


def transform(response: requests.Response) -> dict[str, Any] | None:
    try:
        data = response.json()

        coin_data = next(iter(data["data"].values()))
        crypto_data = next(iter(coin_data))
        quote_dict = crypto_data["quote"]
        base_currency = next(iter(quote_dict))
        quote_data = quote_dict[base_currency]

        return {
            "symbol": crypto_data.get("symbol"),
            "last_updated": quote_data.get("last_updated"),
            "base_currency": base_currency,
            "price": quote_data.get("price"),
            "circulating_supply": crypto_data.get("circulating_supply"),
            "total_supply": crypto_data.get("total_supply"),
            "market_cap": quote_data.get("market_cap"),
            "market_cap_dominance": quote_data.get("market_cap_dominance"),
            "fully_diluted_market_cap": quote_data.get("fully_diluted_market_cap"),
            "percent_change_1h": quote_data.get("percent_change_1h"),
            "percent_change_24h": quote_data.get("percent_change_24h"),
            "percent_change_7d": quote_data.get("percent_change_7d"),
            "percent_change_30d": quote_data.get("percent_change_30d"),
            "percent_change_60d": quote_data.get("percent_change_60d"),
            "percent_change_90d": quote_data.get("percent_change_90d"),
            "volume_24h": quote_data.get("volume_24h"),
            "volume_change_24h": quote_data.get("volume_change_24h"),
            "cmc_rank": crypto_data.get("cmc_rank"),
        }

    except (StopIteration, AttributeError, TypeError):
        return None
