https://hongqq.medium.com/basic-trading-code-for-ib-ib-sync-7a2182c2973c

from ib_insync import *
import time
import numpy as np

# Connect to Interactive Brokers
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

# Define the contract
contract = Future('MES', '202403', 'CME')

# Define trading parameters
quantity = 1
short_sma_period = 5  # Short-term SMA period
long_sma_period = 20  # Long-term SMA period

# Calculate Simple Moving Averages
def calculate_sma(data, window):
    return np.convolve(data, np.ones(window), 'valid') / window

# Define entry criteria
def should_enter_trade(short_sma, long_sma):
    return True #short_sma[-1] > long_sma[-1] and short_sma[-2] <= long_sma[-2]

# Define exit criteria
def should_exit_trade(short_sma, long_sma):
    return short_sma[-1] < long_sma[-1] and short_sma[-2] >= long_sma[-2]

# Main trading loop
while True:
    # Fetch historical data
    bars = ib.reqHistoricalData(contract, endDateTime='', durationStr='2 D',
                                barSizeSetting='1 min', whatToShow='MIDPOINT', useRTH=True)

    # Calculate SMAs
    prices = [bar.close for bar in bars]
    short_sma = calculate_sma(prices, short_sma_period)
    long_sma = calculate_sma(prices, long_sma_period)

    if len(short_sma) > 1 and len(long_sma) > 1:
        # Check for entry signal
        if should_enter_trade(short_sma, long_sma):
            # Place buy order
            order = MarketOrder('BUY', quantity)
            trade = ib.placeOrder(contract, order)

            # Wait for exit signal
            while True:
                # Fetch new market data
                new_bars = ib.reqHistoricalData(contract, endDateTime='', durationStr='2 D',
                                                barSizeSetting='5 mins', whatToShow='MIDPOINT', useRTH=True)
                new_prices = [bar.close for bar in new_bars]
                new_short_sma = calculate_sma(new_prices, short_sma_period)
                new_long_sma = calculate_sma(new_prices, long_sma_period)

                if should_exit_trade(new_short_sma, new_long_sma):
                    # Place sell order
                    order = MarketOrder('SELL', quantity)
                    ib.placeOrder(contract, order)
                    break

    # Sleep to avoid hitting rate limits
    time.sleep(300)

# Disconnect from Interactive Brokers
ib.disconnect()
