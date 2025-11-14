import os

import dotenv

dotenv.load_dotenv()

BASE_URL = "https://api.coingecko.com/api/v3/simple/price"

# این اسمش همون قبلی می‌مونه ولی الان لیست CoinGecko IDs است نه سمبل CMC
COINMARKETCAP_SYMBOLS = "bitcoin,ethereum,solana"  # مثلا BTC, ETH, SOL


COINMARKETCAP_API_KEY = os.getenv("COINMARKETCAP_API_KEY", "")


UPDATE_FREQ_SEC = int(os.getenv("UPDATE_FREQ_SEC", 60))
