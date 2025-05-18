import yfinance as yf

# Example: Get historical data for Apple
stock_data = yf.download("AAPL", start="2020-01-01", end="2024-01-01", interval="1d")

#Example of loading stock data via yfinance
print(stock_data)