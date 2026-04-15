import pandas as pd

df2 = pd.read_csv("../portfolio.csv")   # Goes into FullProgram and searches for portfolio.csv
print(df2)
print(df2.describe())
# .describe() fxn gives you these 8 variables: count, mean, std, min, man, 25%, 50%, and 75%.
# also no ticker column because .describe() only deals with numeric columns no string.

df2["value"] = (df2["price"] * df2["quantity"]).round(2)
print(df2.sort_values("value", ascending=False))
print(f"\nBest performer: {df2.loc[df2['value'].idxmax(), 'ticker']}")  # .idxmax() finds index of highest value & .loc() gets the ticker from that row. aka locate
print(f"Total Portfolio: ${df2['value'].sum():,.2f}")
# {df2.loc[df2['value'].idxmax(), 'ticker']}") -> this means locate the max value and its ticker.

df2.to_csv("analysis_report.csv", index=False)  # index=false means dont save the row numbers. It will reduce clutter in .csv
print("Report Saved!")
