import yfinance as yf
import pandas as pd
from ta.momentum import TSIIndicator



# Rearrange the signal conditions
# Do not use this function yet

def TSIsignal(stock_symbol, start_date, end_date):
    # Fetch historical data for the specified date range
    ticker = yf.Ticker(stock_symbol)
    historical_data = ticker.history(start=start_date, end=end_date)

    # Calculate TSI
    tsi_period = 13
    tsi_indicator = TSIIndicator(close=historical_data['Close'], window_slow=25, window_fast=13)
    historical_data['tsi'] = tsi_indicator.tsi()

    # Generate signals
    historical_data['tsi_signal'] = 0  # 0 represents no signal

    # Buy signal: TSI crosses above 0
    historical_data.loc[historical_data['tsi'] > 0, 'tsi_signal'] = 1

    # Sell signal: TSI crosses below 0
    historical_data.loc[historical_data['tsi'] < 0, 'tsi_signal'] = -1

    # Filter out rows with 0 values
    signals_df = historical_data.loc[historical_data['tsi_signal'] != 0, ['Close', 'tsi', 'tsi_signal']]

    return signals_df