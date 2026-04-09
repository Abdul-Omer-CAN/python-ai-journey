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


# DAY 1 Project P&L Calculator

company = input("Abdulrehman Corp")
revenue = float(input("14500000"))
cogs = float(input("40000"))  # cost of the goods
opex = float(input("250000"))  # cost of operating expenses
tax_rate = float(input("0.21"))  # tax rate

# Calculations

gross_profit = revenue-cogs
gross_margin = gross_profit/revenue
ebit = gross_profit-opex  # Ebit is earnings before interest and tax
tax_amount = ebit*tax_rate
net_profit = ebit-tax
net_margin = net_profit/revenue

# Determine Health

if net_margin > 0.20:
    verdict = "Excellent"
elif net_margin > 0.10:
    verdict = "Healthy"
elif net_margin > 0:
    verdict = "Marginal"
else:
    verdict = "At a Loss"

# Output Report

print(f"\n{'='*40}")  # /n means to add a blank line & *40 multiplies = by 40 giving us 40 equal signs.
print(f" P&L Report -- {company}")  # the reason why we add f" is because it will detect {company} without it it will just print {company} literally.
print(f"{'='*40}")
print(f"    Revenue    ${revenue:>12,.2f}")
# : means the next instructions are for formating
# >12 this means right align all the number to 12 characters.
# , add comma where appropriate
# .2f shows 2 decimal places after the number .00
