import yfinance as yf
import pandas as pd
from ta.momentum import stoch_signal

def get_historical_data(stock_symbol, period='1d', interval='1m'):
    ticker = yf.Ticker(stock_symbol)
    return ticker.history(period=period, interval=interval)

def SMIsignal(data, smi_period=14, signal_line_period=3):
    # Calculate the SMI
    data['smi'] = stoch_signal(data['Close'], data['Close'], window=smi_period)

    # Calculate the signal line
    data['signal_line'] = data['smi'].rolling(window=signal_line_period).mean()

    last_smi = data['smi'].iloc[-1]
    last_signal_line = data['signal_line'].iloc[-1]

    print(f"Last SMI value: {last_smi}")
    print(f"Last Signal line value: {last_signal_line}")

    if last_smi > last_signal_line and data['smi'].iloc[-2] <= data['signal_line'].iloc[-2]:
        return "Buy Signal"
    elif last_smi < last_signal_line and data['smi'].iloc[-2] >= data['signal_line'].iloc[-2]:
        return "Sell Signal"
    else:
        return "No clear signal"

def get_real_time_price(stock_symbol):
    historical_data = get_historical_data(stock_symbol)
    
    signal = SMIsignal(historical_data)
    print(f"SMI Signal: {signal}")

    ticker = yf.Ticker(stock_symbol)
    real_time_data = ticker.info
    real_time_price = real_time_data.get('currentPrice', None)

    if real_time_price is not None:
        print(f"Real-time price of {stock_symbol}: ${real_time_price}")
    else:
        print(f"Unable to retrieve real-time price for {stock_symbol}")

if __name__ == "__main__":
    # Replace 'AAPL' with your stock symbol
    stock_symbol = 'FROTO.IS'

    # Call the function to get real-time price and check SMI signals
    get_real_time_price(stock_symbol)
