from binance.client import Client

api_key = 'your_api_key'
api_secret = 'your_api_secret'

client = Client(api_key, api_secret)

# Parameters
symbol = "BTCUSDT"  # Symbol to trade
quantity = 0.01  # Quantity to trade (in BTC)
interval = "1h"  # Interval for retrieving historical price data
mean_reversion_threshold = 0.05  # Threshold for mean reversion strategy
stop_loss_threshold = -0.1  # Stop loss threshold for closing position