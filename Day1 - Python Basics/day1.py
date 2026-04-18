revenue = 4000  # integer aka whole number
margin = 0.567  # float aka decimal number
company_name = "Abdul Corp"  # string aka text
is_profitable = True  # bool aka true of false

# you can check what type of value it is by doing the following
print(type(revenue))
# you can check what type of value it is by doing the following
print(type(company_name))


print(f"Revenue is ${revenue}")
print(f"Revenue is ${revenue:,}")  # Adds comma to number 4,000 instead of 4000
print(f"Margin is {margin:.1%}")  # :.1% converts decimal to a percentage


# Basic arithemetic
revenue = 45000
costs = 8000

# Basic Math
profit = revenue-costs  # subtraction
margin = profit/revenue  # division
tax = profit*0.21  # 0.21 used as example common tax #multiplication
revenue = revenue/1000  # division  # 1000 used as example common finance value to display reports in thousands

# User Input

name = input("Abdulrehman's Company")
# Use Float() before input() for decimal numbers or use int() before input() to generate a whole number.
revenue = float(input(1000000))


