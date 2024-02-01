import yfinance as yf
from ta.momentum import RSIIndicator, StochRSIIndicator


# Prints & returns array of buy or sell signals
# Buy signals represented with '1', sell signals are with '-1'
# If the purpose is check only today just set start_date and end_date as the same value

def StochRSIsignal(stock_symbol, start_date, end_date):
    # Fetch historical data for the specified date range
    ticker = yf.Ticker(stock_symbol)
    historical_data = ticker.history(start=start_date, end=end_date)

    # Calculate RSI
    rsi_period = 14
    rsi_indicator = RSIIndicator(close=historical_data['Close'], window=rsi_period)
    historical_data['rsi'] = rsi_indicator.rsi()

    # Calculate Stochastic RSI
    stoch_rsi_period = 14
    stoch_rsi_indicator = StochRSIIndicator(close=historical_data['rsi'], window=stoch_rsi_period)
    historical_data['stoch_rsi_d'] = stoch_rsi_indicator.stochrsi_d()
    historical_data['stoch_rsi_k'] = stoch_rsi_indicator.stochrsi_k()

    # Generate signals
    historical_data['stoch_rsi_signal'] = 0  # 0 represents no signal

    # Identify buy signals
    buy_condition = (historical_data['stoch_rsi_k'].shift(1) < historical_data['stoch_rsi_d'].shift(1)) & (historical_data['stoch_rsi_k'] > historical_data['stoch_rsi_d'])
    historical_data.loc[buy_condition, 'stoch_rsi_signal'] = 1

    # Identify sell signals
    sell_condition = (historical_data['stoch_rsi_k'].shift(1) > historical_data['stoch_rsi_d'].shift(1)) & (historical_data['stoch_rsi_k'] < historical_data['stoch_rsi_d'])
    historical_data.loc[sell_condition, 'stoch_rsi_signal'] = -1

    # Filter out rows with 0 values and ensure 'stoch_rsi' is present in the DataFrame
    if 'stoch_rsi' in historical_data.columns:
        signals_df = historical_data.loc[historical_data['stoch_rsi_signal'] != 0, ['Close', 'stoch_rsi', 'stoch_rsi_signal']]
    else:
        signals_df = historical_data.loc[historical_data['stoch_rsi_signal'] != 0, ['Close', 'stoch_rsi_d', 'stoch_rsi_k', 'stoch_rsi_signal']]

    return signals_df