import yfinance as yf
import pandas as pd
from ta.trend import MACD

def MACDsignal(stock_symbol):
    # Creating a Ticker object
    ticker = yf.Ticker(stock_symbol)

    # Get historical data
    historical_data = ticker.history(period='1d', interval='1m')

    # Calculate MACD
    macd = MACD(historical_data['Close'])

    # Accessing MACD and Signal line values
    macd_value = macd.macd()
    signal_line = macd.macd_signal()

    # Print the last MACD and Signal line values (currency is $)
    print(f"Last MACD value: {macd_value.iloc[-1]}")
    print(f"Last Signal line value: {signal_line.iloc[-1]}")

    # Check if MACD crossed above Signal line (potential buy signal)
    if macd_value.iloc[-1] > signal_line.iloc[-1] and macd_value.iloc[-2] <= signal_line.iloc[-2]:
        print("Potential Buy Signal!")
    # Check if MACD crossed below Signal line (potential sell signal)
    elif macd_value.iloc[-1] < signal_line.iloc[-1] and macd_value.iloc[-2] >= signal_line.iloc[-2]:
        print("Potential Sell Signal!")
    else:
        print("No clear signal.")

    # Get real-time data
    real_time_data = ticker.info

    # Access a specific key, for example, 'regularMarketPrice'
    real_time_price = real_time_data.get('currentPrice', None)

    # Printing the real-time price
    #if real_time_price is not None:
        #print(f"Real-time price of {stock_symbol}: {real_time_price}")
    #else:
        #print(f"Unable to retrieve real-time price for {stock_symbol}")

