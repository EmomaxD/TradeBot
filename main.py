from MACD import MACDsignal
from SMI import SMIsignal
import yfinance as yf

def get_real_time_price(stock_symbol):
    
    ticker = yf.Ticker(stock_symbol)
    real_time_data = ticker.info
    real_time_price = real_time_data.get('currentPrice', None)

    if real_time_price is not None:
        print(f"Real-time price of {stock_symbol}: {real_time_price}₺")
    else:
        print(f"Unable to retrieve real-time price for {stock_symbol}")




#print(real_time_data.keys())


stock_symbol = 'FROTO.IS'

MACDsignal(stock_symbol)


#signal = SMIsignal(stock_symbol)
#print("SMI signal: " + signal)     !!! FIX


get_real_time_price(stock_symbol)