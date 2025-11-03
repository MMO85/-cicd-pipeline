import os

import dotenv

dotenv.load_dotenv()

COINMARKETCAP_API_KEY = os.getenv("COINMARKETCAP_API_KEY", "")
COINMARKETCAP_SYMBOLS = os.getenv("COINMARKETCAP_SYMBOLS", "BTC")

UPDATE_FREQ_SEC = int(os.getenv("UPDATE_FREQ_SEC", 60))
