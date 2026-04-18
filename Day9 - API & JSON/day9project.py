import yfinance as yf  # import yfinance library to get live data for our stocks
import pandas as pd   # import pandas tools to create the dataframe

portfolio = {                  # My portfolio
    "AAPL": 10,
    "GOOGL": 5,
    "TSLA": 8,
    "MSFT": 3
}

print("Fetching live prices...\n")

results = []                    # This will be our results and wwe will add using .append()

for ticker, quantity in portfolio.items():   # ticker and quantity are the two items in our portfolio
    stock = yf.Ticker(ticker)                # focus on this specific stock e.g yf.Ticker('APPL')
    price = stock.info.get("regularMarketPrice", 0)     # grab the current price of the stock via .info[key]
    value = price * quantity                 # our value will be the price * quantity
    results.append({                         # add these to our results using .append({})
        "ticker": ticker,
        "price": price,
        "quantity": quantity,
        "value": value
    })

df = pd.DataFrame(results)    # converts the result into a pandas dataframe.
df = df.sort_values("value", ascending=False)  # sorts values high to low.

print(df.to_string(index=False))  # prints the dataframe as a clean string with no index
print(f"\nTotal Portfolio Value: ${df['value'].sum():,.2f}")  # Adds all values and prints the total value of the portfolio.


### New functions learnt today: ###
# requests.get(url) -> visits the url and grabs the data
# response.status_code -> tells you if the request went through. 200 means it did. 404 means not found or 500 service error.
# response.json() -> converts the API data into a dictionary
# yf.Ticker("") -> focuses on the object in brackets
# .items() -> loops through each item and gives us a key and value
# get() -> lookups the dictionary safely without crashing if not found will give zero. Must add ',0'
# API Stands for Application Programming Interface
# JSON = Javascript Object notation | most common format of data sent over the internet.
# e.g is 'yfinance' is the library and it connects to Yahoo finance's API with 'yf.Ticker'.
# yf.Ticker is ONLY Specific to yfinance each API's have there own class.
