import pandas as pd  # imported pandas as pd so that we read .csv files
import matplotlib.pyplot as plt  # so that we can create charts and use their functions

# Load real data

df = pd.read_csv("../Day5/portfolio.csv")  # read your portfolio.csv to the dataframe
df["value"] = df["price"] * df["quantity"]  # add a new column called value - in it (price * quantity) for each stock.

# Create a figure with 2 charts side by side

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
# ^ create a figure with 2 figure ax1 and ax2. 2 figures by using plt.subplots and it will contain
# 1 row and 2 column & figure size will be 12 inches wide and 5 inches tall.


# Chart 1 - Bar chart of portfolio values

ax1.bar(df["ticker"], df["value"], color=["blue", "green", "red", "orange"])
# ^ bar chart assigned to ax1 and it will pull 2 variables from the dataframes ticker which will be x axis and
# value which will be on the y axis and each bar gets its own color

ax1.set_title("Portfolio Values")  # title for the ax1 chart
ax1.set_xlabel("Stock")  # x label for the ax1 chart is stock
ax1.set_ylabel("Value ($)")  # y label for the ax1 cahrt is value
ax1.grid(True, axis="y")  # grid lines on the y axis only makes it look better

# Chart 2 - Pie chart of allocation

ax2.pie(df["value"], labels=df["ticker"], autopct="%1.1f%%", startangle=90)
# ^ ax2 will be our pie chart. our slice sizes will be determined via "values". The labels on the pie chart
# ^will be determined by "ticker". autopercentage will be on them 1 number before and after decimal with a
# ^% sign at the end. the pie chart will start its first slice at a 90 degree angle on the top.

ax2.set_title("Portfolio Allocation")  # title set to portfolio allocation
plt.suptitle("My Stock Portfolio Dashboard", fontsize=16)  # One big title for both charts at the top aka supertitle
plt.tight_layout()  # optimizes our chart elements mentioned below as well
plt.show()  # show the chart! just like def main() and then main() at the end.

## All new functions learnt today ##
# plt.plot() - line chart
# plt.bar()- bie chart
# plt.pie() - pie chart
# plt.subplots() - multiple charts
# plt.set_title/xlabel/ylabel - Labels
# plt.grid() - add grid lines
# plt.tight_layout() - optimzes all elements in the chart
# autopct - autopercentage mostly '%1.1f%%'
# ax1/ax2 - use functions on ax1 aka first graph or ax2 seond graph
