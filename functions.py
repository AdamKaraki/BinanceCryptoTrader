import time
import binance
from config import client, symbol, quantity, interval, mean_reversion_threshold, stop_loss_threshold

# Function to retrieve historical price data
def get_historical_data():
    klines = client.get_historical_klines(symbol, interval, "30 days ago")
    return [[float(kline[1]), float(kline[4])] for kline in klines]

# Function to calculate mean and standard deviation of historical price data
def calculate_statistics(historical_data):
    prices = [data[1] for data in historical_data]
    mean = sum(prices) / len(prices)
    stdev = (sum([(price - mean) ** 2 for price in prices]) / len(prices)) ** 0.5
    return mean, stdev

# Function to check if price is below mean by a certain threshold
def is_below_mean(price, mean, stdev, threshold):
    return price < mean - (threshold * stdev)

# Function to check if price is above mean by a certain threshold
def is_above_mean(price, mean, stdev, threshold):
    return price > mean + (threshold * stdev)

# Function to place a limit buy order
def place_buy_order(price):
    buy_price = round(price * 0.99, 2)  # Place limit order 1% below current price
    order = client.order_limit_buy(
        symbol=symbol,
        quantity=quantity,
        price=buy_price)
    return order

# Function to place a limit sell order
def place_sell_order(price):
    sell_price = round(price * 1.01, 2)  # Place limit order 1% above current price
    order = client.order_limit_sell(
        symbol=symbol,
        quantity=quantity,
        price=sell_price)
    return order

# Function to get the current price
def get_current_price():
    ticker = client.get_symbol_ticker(symbol)
    price = float(ticker["price"])
    return price
