import pandas as pd   # basically says import pandas specialized tools as pd

data = {                     # REASON why we use {} is because we are inputting in a dictionary
    "ticker": ["APPL", "GOOGL", "TSLA", "MSFT", "AMZN"],
    "price": [182.50, 141.20, 245.80, 378.90, 156.30],
    "quantity": [10, 5, 8, 3, 7]
}
# Also python is very case sensitive (DataFrame) Frame's F is capital so becareful below
df = pd.DataFrame(data)  # frames the data and makes it into a table
print(df)
