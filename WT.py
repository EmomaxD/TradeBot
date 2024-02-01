import yfinance as yf
import pandas as pd

# Helper functions

def ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def sma(data, window):
    return data.rolling(window=window).mean()






# Prints & returns array of buy or sell signals
# Buy signals represented with '1', sell signals are with '-1'
# If the purpose is check only today just set start_date and end_date as the same value

def WTsignal(stock_symbol, start_date, end_date):

    df = yf.download(stock_symbol, start=start_date, end=end_date)

    n1 = 10
    n2 = 21

    # Calculate necessary values
    ap = df['Close']
    esa = ema(ap, n1)
    d = ema(abs(ap - esa), n1)
    ci = (ap - esa) / (0.015 * d)
    tci = ema(ci, n2)

    wt1 = tci
    wt2 = sma(wt1, 4)

    # Create a DataFrame to store the signals
    signals = pd.DataFrame(index=df.index)

    # Add signals based on conditions
    signals['Buy_Signal'] = (wt1 > wt2) & (wt1.shift(1) <= wt2.shift(1))
    signals['Sell_Signal'] = (wt1 < wt2) & (wt1.shift(1) >= wt2.shift(1))

    # Map signals to numerical values
    signals['Signal'] = signals['Buy_Signal'].astype(int) - signals['Sell_Signal'].astype(int)

    # Print signals only when there's a clear signal (1 or -1)
    clear_signals = signals[signals['Signal'] != 0]['Signal']
    if not clear_signals.empty:
        print(clear_signals.values)

    return clear_signals
