import yfinance as yf
def get stock_data(ticker):
data = yf.download(ticker, period='1mo')
return data
 print(get_stock_data('RELIANCE.NS))
