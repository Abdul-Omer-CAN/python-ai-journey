import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

df = pd.read_csv("../Day5 - File-IO-CSV/portfolio.csv")

sectors = {
    "AAPL": "Technology",
    "GOOGL": "Technology",
    "TSLA": "Automotive",
    "MSFT": "Technology"
}

df["sector"] = df["ticker"].map(sectors)  # Adds a new column to the df called sector

print(df)

print("Fetching live prices....")


results = []

for index, row in df.iterrows():  # .iterrows gives you 2 things index no. and row data.
    ticker = row["ticker"]
    buy_price = row["price"]
    quantity = row["quantity"]

    stock = yf.Ticker(ticker)
    live_price = stock.info.get("regularMarketPrice", 0)

    current_value = live_price * quantity
    cost = buy_price * quantity
    gain_loss = current_value - cost
    return_pct = (gain_loss / cost) * 100

    results.append({
        "ticker": ticker,
        "sector": row["sector"],
        "buy_price": buy_price,
        "quantity": quantity,
        "live_price": round(live_price, 2),
        "current_value": round(current_value, 2),
        "cost": round(cost, 2),
        "gain_loss": round(gain_loss, 2),
        "return_pct": round(return_pct, 2)
    })

results_df = pd.DataFrame(results)
print(results_df)

sector_summary = results_df.groupby("sector")[["current_value", "gain_loss"]].sum()  # w/ double brackets you can select multiple columns
print(sector_summary)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.bar(results_df["ticker"], results_df["gain_loss"])
ax1.set_title("Gain/Loss per stock")
ax1.set_ylabel("Gain/loss")
ax1.set_xlabel("Stock")
ax1.grid(True, axis="y")

ax2.pie(sector_summary["current_value"], labels=sector_summary.index, autopct="%1.1f%%")
ax2.set_title("Portfolio value by sector")
plt.suptitle("My Stock Portfolio", fontsize=16)

plt.tight_layout()
plt.show()
print(f"{ticker} | Live: {live_price:.2f} | Cost: {cost:.2f} | Value: {current_value:.2f} | Gain: {gain_loss:.2f} | Return: {return_pct:.2f}%")

results_df.to_csv("portfolio_summary.csv", index=False)
print("Summary exported to portfolio_summary.csv")


## Summary ##
# Load portfolio from CSV
# Fetch live prices via yfinance
# Calculate returns + sector analysis with Pandas
# Visualise with Matplotlib bar + pie charts
# Export summary to portfolio_summary.csv
