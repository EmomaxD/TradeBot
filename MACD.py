import yfinance as yf
import pandas as pd
from ta.trend import MACD

def MACDsignal(stock_symbol, startDate, endDate):
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
        return true
    # Check if MACD crossed below Signal line (potential sell signal)
    elif macd_value.iloc[-1] < signal_line.iloc[-1] and macd_value.iloc[-2] >= signal_line.iloc[-2]:
        print("Potential Sell Signal!")
    else:
        print("No clear signal.")




