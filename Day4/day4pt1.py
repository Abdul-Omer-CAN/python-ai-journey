# Day 4 our goal is to make a program for stocks


# stocks = ["APPL", "GOOGLE", "TSLA", "MSFT"]  # This [] is used for listing each variable has a position
# print(stocks[0])  # position 0 is apple - position 1 is google etc..
# print(stocks[-1])
# print(len(stocks))  # len lets us know how many variables are stored in a variable which in our case is 4
# stocks.append("AMZN")  # append adds it to out list
# print(stocks)

### Exercise ###

# stock = {
#     "ticker": "APPL",
#     "price": 182.50,
#     "quantity": 10
# }

# print(stock["ticker"])
# print(stock["price"])
# print(stock["quantity"])


# # Calculating the total Value

# total_value = stock["price"] * stock["quantity"]
# print(f"{stock["ticker"]} total value: ${total_value:,.2f}")


### Portfolio Exercise ###

# portfolio = [
#     {"ticker": "APPL", "price": 182.5, "quantity": 10},
#     {"ticker": "GOOGL", "price": 141.20, "quantity": 5},
#     {"ticker": "TSLA", "price": 245.80, "quantity": 8},
#     {"ticker": "MSFT", "price": 378.90, "quantity": 3}
# ]


# print(f"{portfolio[2]["ticker"]}: ${portfolio[2]['price']}")   # You can only have 1 experession per {} if more add more {} in one f string
# print(portfolio[0]['ticker'])
# print(portfolio[2]['price'])
# print(portfolio[3]["quantity"])


# print(portfolio[0]["ticker"])           # No loop tedious this is just for ticker lol look at line 40 imagine doing that for each
# print(portfolio[1]["ticker"])
# print(portfolio[2]["ticker"])
# print(portfolio[3]["ticker"])


# for stock in portfolio:  # This is a loop it automatically run the code for each line and gives us the answer
#     value = stock["price"] * stock["quantity"]  # key here is for "---- in -----" in line 52 thisis what triggers python to run each line automatically
#     print(f"{stock['ticker']}: ${value:,.2f}")


##### Listing exercise #######

# values = [1825.00, 706.00, 1966.40, 1136.70]

# print(max(values))
# print(min(values))
# print(sum(values))
# print(sorted(values))      # sorted is always from smallest to largest


### try/except ###

age = int(input("Enter Age here: "))   # Program will crash if you enter for example 'abc'. Use try/except instead


try:
    age = int(input("Enter Age here: "))    # Program will run and give you an output saying that it is invalid
    print(f"Your age is {age}")
except ValueError:
    print("That is not a valid number")
