import pandas as pd

# Load the data onto this file and df stands for dataframe. Its most commonly used

df = pd.read_csv("stocks_data.csv")  # .read_csv means read the following file in ()


# data is below:

print(df.head())    # prints the first 5 row
print(df.shape)     # prints the number of rows and columns
print(df.dtypes)    # prints the data types of each column
print(df.describe())  # Gives us a stat summary
print(df["sector"].unique())  # .unique() removes the duplicates for only 'sector'
print(df["ticker"].value_counts())  # .value_counts() tells us how many times a value is repeated
print(df.isnull().sum())  # .isnull() tells us if there is a missing value in a cell. and .sum() will give us a total.
# .isnull().sum() a key tool data scientists use to catch any missing values aka data cleaning


sector_avg = df.groupby("sector")["price"].mean()  # groupby will group all rows together and calculate the mean
print(sector_avg)  # print the sector_avg


# more groupby operations

sector_volume = df.groupby("sector")["volume"].sum()
print(sector_volume)

# .agg([]) adds multiple functions at once
sector_stats = df.groupby("sector")["price"].agg(["mean", "max", "min"])
print(sector_stats)
