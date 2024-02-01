from MACD import MACDsignal
from SMI import SMIsignal
from TSI import TSIsignal
from Fisher import Fishersignal
from RSI import RSIsignal
from StochRSI import StochRSIsignal
from WT import WTsignal

from datetime import datetime
import yfinance as yf

def get_real_time_price(stock_symbol):
    
    ticker = yf.Ticker(stock_symbol)
    real_time_data = ticker.info
    real_time_price = real_time_data.get('currentPrice', None)

    if real_time_price is not None:
        print(f"Real-time price of {stock_symbol}: {real_time_price}₺")
    else:
        print(f"Unable to retrieve real-time price for {stock_symbol}")




# Get today's date
today_date = datetime.today().strftime('%Y-%m-%d')

start_date = '2023-01-01' # for backtesting

#print(real_time_data.keys())


stock_symbol = 'FROTO.IS'


#MACDsignal(stock_symbol, start_date, today_date)

#########
#tsi_signals = TSIsignal(stock_symbol, start_date, today_date)
#print(tsi_signals)
#########

#########
#rsi_signals = RSIsignal(stock_symbol, start_date, today_date)
#print(rsi_signals)
#########

#########
#stoch_rsi_signals = StochRSIsignal(stock_symbol, start_date, today_date)
#print(stoch_rsi_signals)
#########

#########                                           !!! FIX !!!
#fisher_signals = Fishersignal(stock_symbol)
#print(fisher_signals)
#########

#########
# Calculate WaveTrend
signals = WTsignal(stock_symbol, start_date, today_date)
print(signals)
#########

get_real_time_price(stock_symbol)