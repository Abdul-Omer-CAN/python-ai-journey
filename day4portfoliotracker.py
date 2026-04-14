## Input Section ##

# portfolio = []

# while True:
#     ticker = input("Enter stock ticker (or 'done' to finish): ").upper()

#     if ticker == "DONE":
#         break
#     try:
#         price = float(input(f"Enter price for {ticker}: $"))
#         quantity = int(input(f"Enter quantity for {ticker}: "))

#         portfolio.append({
#             "ticker": ticker,
#             "price": price,
#             "quantity": quantity
#         })
#         print(f"{ticker} added! ✅")

#     except ValueError:
#         print("Invalid Input - Please enter valid numbers! ")

## Input section using .csv file - i deactivated the inital one you activate one or the other ##

import csv

portfolio = []

with open("portfolio.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        portfolio.append({
            "ticker": row[0],
            "price": float(row[1]),
            "quantity": int(row[2])
        })


## Process Section ##


total_portfolio_value = 0
values = []

for stock in portfolio:
    value = stock["price"] * stock["quantity"]
    values.append(value)
    total_portfolio_value += value

best_value = max(values)
worst_value = min(values)


# Find best and worst performers

for stock in portfolio:
    value = stock["price"] * stock['quantity']
    if value == best_value:                # '==' is asking this " Is value the same as best_value Yes or NO"
        best_stock = stock["ticker"]
    if value == worst_value:
        worst_stock = stock["ticker"]

     ## Output Section ###

print(f"\n{'='*50}")
print(f"            STOCK PORTFOLIO REPORT")
print(f"{'='*50}")

for stock in portfolio:
    value = stock['price'] * stock["quantity"]
    print(f"   {stock['ticker']:6} | ${stock['price']:>10,.2f} x {stock['quantity']:>4} = ${value:>12,.2f}")

print(f"{'='*50}")
print(f"  Total Portfolio Value:    ${total_portfolio_value:>12,.2f}")
print(f"  Best Performer:           {best_stock}")
print(f"  Worst Performer:          {worst_stock}")
print(f"{'='*50}\n")
