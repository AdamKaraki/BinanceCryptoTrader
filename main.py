from config import *
from functions import *


# Main loop
while True:
    try:
        # Retrieve historical price data
        historical_data = get_historical_data()

        # Calculate mean and standard deviation
        mean, stdev = calculate_statistics(historical_data)

        # Get current price
        price = get_current_price()

        # Check if price is below mean by threshold
        if is_below_mean(price, mean, stdev, mean_reversion_threshold):
            # Place buy order
            print(f"Placing buy order at {price:.2f}")
            order = place_buy_order(price)

            # Wait for order to fill
            while True:
                order_status = client.get_order(
                    symbol=symbol,
                    orderId=order["orderId"])
                if order_status["status"] == "FILLED":
                    print(f"Buy order filled at {order_status['price']}")
                    break
                else:
                    time.sleep(1)

            # Place stop loss order
                        # Place stop loss order
            # Place stop loss order
            stop_loss_price = round(order_status["price"] * (1 + stop_loss_threshold), 2)
            stop_loss_order = client.create_oco_order(
                symbol=symbol,
                quantity=quantity,
                side=binance.enums.SIDE_SELL,
                stopLimitTimeInForce=binance.enums.TIME_IN_FORCE_GTC,
                stopLimitPrice=stop_loss_price,
                stopPrice=stop_loss_price * 0.98,  # Set stop price 2% below stop limit price
                price=price * 0.95,  # Set take profit price 5% below current price
                type=binance.enums.ORDER_TYPE_STOP_LOSS_LIMIT,
                )

            print(f"Stop loss order placed at {stop_loss_price}")

        # Check if price is above mean by threshold
        elif is_above_mean(price, mean, stdev, mean_reversion_threshold):
            # Place sell order
            print(f"Placing sell order at {price:.2f}")
            order = place_sell_order(price)

            # Wait for order to fill
            while True:
                order_status = client.get_order(
                    symbol=symbol,
                    orderId=order["orderId"])
                if order_status["status"] == "FILLED":
                    print(f"Sell order filled at {order_status['price']}")
                    break
                else:
                    time.sleep(1)

            # Place stop loss order
            stop_loss_price = round(order_status["price"] * (1 - stop_loss_threshold), 2)
            stop_loss_order = client.create_oco_order(
                symbol=symbol,
                quantity=quantity,
                side=binance.enums.SIDE_SELL,
                stopLimitTimeInForce=binance.enums.TIME_IN_FORCE_GTC,
                stopLimitPrice=stop_loss_price,
                stopPrice=stop_loss_price * 0.98,  # Set stop price 2% below stop limit price
                price=price * 0.95,  # Set take profit price 5% below current price
                type=binance.enums.ORDER_TYPE_STOP_LOSS_LIMIT,
                )

            print(f"Stop loss order placed at {stop_loss_price}")

        # Wait for next interval
        time.sleep(3600)

    except Exception as e:
        print(e)
        time.sleep(60)
