#Crypto Trading Bot
This project is a simple crypto trading bot that utilizes the Binance API to get information about markets and execute trades. The bot uses a mean reversion strategy to identify potential buying opportunities and sets a stop loss threshold to minimize losses.

##Getting Started
To use the bot, you will need to have a Binance account and generate an API key and secret. You will also need to install the python-binance library using pip install python-binance.

##Clone the repository to your local machine.
Create a virtual environment and activate it.
Install the required dependencies using pip install -r requirements.txt.
Open config.py and add your Binance API key and secret.
Customize the parameters in main.py such as symbol, quantity, interval, mean_reversion_threshold, and stop_loss_threshold.
Run python main.py to start the bot.

##Parameters
symbol: The trading pair to use, e.g. "BTCUSDT".
quantity: The quantity to trade, e.g. 0.01 BTC.
interval: The interval for retrieving historical price data, e.g. "1h".
mean_reversion_threshold: The threshold for mean reversion strategy, e.g. 0.05.
stop_loss_threshold: The stop loss threshold for closing position, e.g. -0.1.

##Strategy
The mean reversion strategy is a simple trading strategy that involves buying an asset when its price is below its historical mean by a certain threshold, and selling the asset when its price is above its historical mean by a certain threshold. The idea is that the price will eventually revert back to its mean, providing a profitable trading opportunity.

In this bot, we use the 1-hour candlestick chart to calculate the historical mean and standard deviation of the trading pair. We then check the current price of the trading pair and determine whether it is below or above the mean by the mean_reversion_threshold. If the price is below the mean, we place a buy order. If the price is above the mean, we do nothing.

To minimize losses, we set a stop loss threshold of stop_loss_threshold. If the price drops below this threshold, we sell the asset to limit our losses.

##Disclaimer
This project is for educational purposes only and does not constitute financial advice. Trading cryptocurrencies involves risks, and you should do your own research before making any investment decisions. The author of this project is not responsible for any losses incurred from using this bot.