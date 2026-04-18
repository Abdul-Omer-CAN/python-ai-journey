import pandas as pd

df = pd.read_csv("stocks_data.csv")

#

df = df.sort_values(["ticker", 'date'])  # Sorts by specific volumn
df["prev_price"] = df.groupby("ticker")["price"].shift(1)
df["daily_return"] = ((df["price"] - df["prev_price"]) / df["prev_price"] * 100).round(2)
print(df[["ticker", "date", "price", "daily_return"]])
# the reason why we used [[]] is because we are accessing a list of variables. list requires it own [].
# if it was only one variable then it would have been a single []

# drops nan values from our results
df_clean = df.dropna()

# Best and worse performer
best = df_clean.loc[df_clean["daily_return"].idxmax()]
worst = df_clean.loc[df_clean["daily_return"].idxmin()]

print(f"\nBest Performer: {best['ticker']} + {best['daily_return']}%")
print(f"Worst Performer: {worst['ticker']} + {worst['daily_return']}%")

# Sector average returns
sector_returns = df_clean.groupby("sector")["daily_return"].mean().round(2)
print(f"\nSector returns: ")
print(sector_returns)

df_clean.to_csv("sector_analysis.csv", index=False)
print("\nReport saved to sector_analysis.csv!")
