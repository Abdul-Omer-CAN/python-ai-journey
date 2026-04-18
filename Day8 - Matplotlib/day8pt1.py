
### PLOT CHART ###
import matplotlib.pyplot as plt
years = [2019, 2020, 2021, 2022, 2023]
revenue = [120, 145, 132, 178, 210]

# Year goes on the x axis and revenue goes on the y axis
# marker"o" add a o at every point | linewidth is the thickness of the line
# plt.grid(True) adds a grid in the background
# plt.tight_layout() automatically adjusts spacing so nothing is cut off
# generates the chart window plt.show()


plt.plot(years, revenue, color="blue", marker="o", linewidth=2)
plt.title("Annual revenue", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Revenue ($000s)", fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()


####### BAR CHART #######
tickers = ["APPL", "GOOGL", "TSLA", "MSFT"]
values = [1900, 706, 1966, 1136]

plt.figure(figsize=(8, 5))  # figsize will put it 8inches wide and 5inches tall
plt.bar(tickers, values, color=["blue", "green", "red", "orange"])  # each bar gets its own color
plt.title("Stock Portfolio Values")
plt.xlabel("Stock")
plt.ylabel("Value ($)")
plt.grid(True, axis="y")  # The grid lines are only on the y axis
plt.tight_layout()
plt.show()


### PIE CHART ###

tickers = ["APPL", "GOOGL", "TSLA", "MSFT"]
values = [1900, 706, 1966, 1136]

plt.figure(figsize=(8, 6))
plt.pie(values, labels=tickers, autopct="%1.1f%%", startangle=90)  # autopct aka automatic percentage
plt.title("Portfolio Allocation")
plt.tight_layout()
plt.show()

# autopct"%1.1f%%" -> % sign is the start of formatting the string | minimum 1 digit before decimal
# and 1f decimal place after | an actual %% sign at the last by doing it twice.

# END
