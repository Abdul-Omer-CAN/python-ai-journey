import pandas as pd   # basically says import pandas specialized tools as pd

data = {                     # REASON why we use {} is because we are inputting in a dictionary
    "ticker": ["APPL", "GOOGL", "TSLA", "MSFT", "AMZN"],
    "price": [182.50, 141.20, 245.80, 378.90, 156.30],
    "quantity": [10, 5, 8, 3, 7]
}
# Also python is very case sensitive (DataFrame) Frame's F is capital so becareful below
df = pd.DataFrame(data)  # frames the data and makes it into a table
# print(df)
print(df["price"])
print(df["price"].mean())
print(df["price"].max())
print(df[df["price"] > 200])

# As you can see from the results Panda is built on top of NumPy e.g. in our code dtype:float64
# NumPy  uses float64 vs Regular python just uses float
# To summarize NumPy is like a engine handles the numbers and maths. Pandas handle table structure, labels, filtering.

# NEW Pandas fxns learnt TODAY:
# pd.DataFrame(data)
# df["column"]
# df["column"].mean()
# df["column"].max()
# df[df["column"] > 200]
# df["new column"] =

# KEY CONCEPTS
#   dtype: float64 -> NumPy data type which is 64bit
#   Dataframe -> a table with row and columns
#   Index -> row of numbers on the left 0,1,2 etc

df["value"] = df["price"] * df["quantity"]  # add a new column called value and it executes price multiply by quantity
print(df)

df_sorted = df.sort_values("value", ascending=False)  # Add .sort_values() to dictionary - it sorts by specific column
print(df_sorted)  # ascending=false -> means big to small - True would be the opposite
