import pandas as pd
import matplotlib.pyplot as plt

# Load real data

df = pd.read_csv("../Day5/portfolio.csv")
df["value"] = df["price"] * df["quantity"]

# Create a figure with 2 charts side by side

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Chart 1 - Bar chart of portfolio values

ax1.bar(df["ticker"], df["value"], color=["blue", "green", "red", "orange"])
ax1.set_title("Portfolio Values")
ax1.set_xlabel("Stock")
ax1.set_ylabel("Value ($)")
ax1.grid(True, axis="y")

# Chart 2 - Pie chart of allocation

ax2.pie(df["value"], labels=df["ticker"], autopct="%1.1f%%", startangle=90)
ax2.set_title("Portfolio Allocation")

plt.suptitle("My Stock Portfolio Dashboard", fontsize=16)
plt.tight_layout()
plt.show()
