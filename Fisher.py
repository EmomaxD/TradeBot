import yfinance as yf
import ta

def Fishersignal(stock_symbol):
    # Fetch historical data
    ticker = yf.Ticker(stock_symbol)
    historical_data = ticker.history(period='1d', interval='1m')

    fisher, trigger = ta.fisher(historical_data, 9)

    return fisher



