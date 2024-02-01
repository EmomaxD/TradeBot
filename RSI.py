import yfinance as yf
import ta
import pandas as pd


# Prints & returns array of buy or sell signals
# Buy signals represented with '1', sell signals are with '-1'
# If the purpose is check only today just set start_date and end_date as the same value

def RSIsignal(stock_symbol, start_date, end_date):
    # Download historical data using yfinance
    data = yf.download(stock_symbol, start=start_date, end=end_date)

    # Calculate RSI using ta library
    data['RSI'] = ta.momentum.RSIIndicator(data['Close'], window=14).rsi()

    # Calculate MA_RSI
    rsi_period = 14
    data['MA_RSI'] = data['RSI'].rolling(window=rsi_period).mean()

    # Calculate previous day's RSI and MA_RSI
    data['Prev_RSI'] = data['RSI'].shift(1)
    data['Prev_MA_RSI'] = data['MA_RSI'].shift(1)

    # Create a column for signals (1 for Buy, -1 for Sell, 0 for no signal)
    data['Signal'] = 0

    # Buy signal: RSI crosses MA_RSI upwards
    buy_condition = (data['RSI'] > data['MA_RSI']) & (data['Prev_RSI'] <= data['Prev_MA_RSI'])
    data.loc[buy_condition, 'Signal'] = 1

    # Sell signal: RSI crosses MA_RSI downwards
    sell_condition = (data['RSI'] < data['MA_RSI']) & (data['Prev_RSI'] >= data['Prev_MA_RSI'])
    data.loc[sell_condition, 'Signal'] = -1

    # Remove rows with no signal (Signal = 0)
    signals = data[data['Signal'] != 0]

    return signals[['Close', 'RSI', 'MA_RSI', 'Signal']]