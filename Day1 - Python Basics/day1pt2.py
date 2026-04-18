# DAY 1 Project P&L Calculator

company = input("Company name: ")
revenue = float(input("Total Revenue ($): "))
cogs = float(input("Cost of goods sold ($): "))  # cost of the goods
opex = float(input("Operating expenses ($): "))  # cost of operating expenses
tax_rate = float(input("Tax rate (e.g. 0.21 for 21%): "))  # tax rate

# Calculations

gross_profit = revenue-cogs
gross_margin = gross_profit/revenue
ebit = gross_profit-opex  # Ebit is earnings before interest and tax
tax_amount = ebit*tax_rate
net_profit = ebit-tax_amount
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

print(f"\n{'='*40}")  # \n means to add a blank line & *40 multiplies = by 40 giving us 40 equal signs.
print(f" P&L Report -- {company}")  # the reason why we add f" is because it will detect {company} without it it will just print {company} literally.
print(f"{'='*40}")
print(f"    Revenue    ${revenue:>12,.2f}")
# : means the next instructions are for formating
# >12 this means right align all the number to 12 characters.
# , add comma where appropriate
# .2f shows 2 decimal places after the number .00
print(f"     COGS          ${cogs:>12,.2f}")
print(f"     Gross Profit  ${gross_profit:>12,.2f}    ({gross_margin:.1%})")  # we gave instructions by adding : and .1% makes it a percentage
print(f"     OPEX          ${opex:>12,.2f}")
print(f"     EBIT          ${ebit:>12,.2f}")
print(f"     TAX           ${tax_amount:>12,.2f}")
print(f"     Net Profit    ${net_profit:>12,.2f}")
print(f"{'='*40}")
print(f"     Verdict: {verdict}")  # we added "Verdict:" before because without that it would only show the verdict function which answer will be Healthy
print(f"{'='*40}\n")  # \n adds a blank line at the end
