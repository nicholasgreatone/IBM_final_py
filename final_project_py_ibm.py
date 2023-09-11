

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# For Apple
apple = yf.Ticker("AAPL")

# Extracting stock info for Apple
apple_info = apple.info
print("Country for Apple:", apple_info['country'])

# Extracting historical share price data for Apple
apple_share_price_data = apple.history(period="max")
print("\nApple Share Price Data (first 5 rows):\n", apple_share_price_data.head())

# Visualizing the Open price against the Date for Apple
apple_share_price_data.reset_index(inplace=True)
apple_share_price_data.plot(x="Date", y="Open", title="Apple Open Price vs. Date")
#plt.show()

# Extracting dividends for Apple
apple_dividends = apple.dividends
print("\nApple Dividends (first 5 rows):\n", apple_dividends.head())

# Plotting dividends over time for Apple
apple.dividends.plot(title="Apple Dividends Over Time")
plt.show()

# For AMD
amd = yf.Ticker("AMD")

# Extract stock info for AMD
amd_info = amd.info
print("\nAMD Stock Info:\n", amd_info['volume'])

amz = yf.Ticker("AMZN")
amz_info = amz.info
amz_his = amz.history(period = 'max')


print("\nAMZN Stock Open Info:\n", amz_his)


#Tesla
tsla = yf.Ticker("TSLA")
ticker_symbol = 'TSLA'
tsla_info = tsla.info
print( f' \n Tesla data:')
tesla_data = yf.download( ticker_symbol, start='2022-01-01', end='2023-01-01')
print(tesla_data)
print(tsla_info)


#Gamestop
ticker_symbol_gme = 'GME'
print (f' \n GME data: ')
gamestop_data = yf.download(ticker_symbol_gme, start='2022-01-01', end='2023-01-01')
print (gamestop_data)



#Tesla
tesla = yf.Ticker('TSLA')
tesla_info = tesla.info
print("Country for Tesla:", tesla_info['country'])
tesla_share_price_data = tesla.history(period="max")
print("\nTesla Share Price Data (first 5 rows):\n", tesla_share_price_data.head())
tesla_share_price_data.reset_index(inplace=True)
tesla_share_price_data.plot(x="Date", y="Open", title="Tesla Revenue over time")
plt.show()



#Gamestop
gamestop = yf.Ticker('GME')
gamestop_info = gamestop.info
print("Country for GameStop:", gamestop_info['country'])
gamestop_share_price_data = gamestop.history(period="max")
print("\nGameStop Share Price Data (first 5 rows):\n", gamestop_share_price_data.head())
gamestop_share_price_data.reset_index(inplace=True)
gamestop_share_price_data.plot(x="Date", y="Open", title="GameStop Revenue over time ")
plt.show()