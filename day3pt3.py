#### 4 Step process for refactoring a program #####

# def get_inputs():  # step 1 get_inputs
#     company = input("Company name: ")
#     revenue = float(input("Total Revenue ($): "))
#     cogs = float(input("Cost of goods sold ($): "))
#     opex = float(input("Operating expenses ($): "))
#     tax_rate = float(input("Tax rate (e.g.0.21 for 21%): "))
#     return company, revenue, cogs, opex, tax_rate


# def calculate(revenue, cogs, opex, tax_rate):  # step 2 def calculate
#     gross_profit = revenue - cogs
#     gross_margin = gross_profit/revenue
#     ebit = gross_profit - opex
#     tax_amount = ebit * tax_rate
#     net_profit = ebit - tax_amount
#     net_margin = net_profit / revenue
#     return gross_profit, gross_margin, ebit, tax_amount, net_profit, net_margin


# def display(company, revenue, cogs, opex, gross_profit, gross_margin, ebit, tax_amount, net_profit, net_margin, verdict):
#     print(f"\n{'='*40}")
#     print(f" P&L Calculator -- {company}")
#     print(f"{'='*40}")
#     print(f"   Revenue:          ${revenue:>12,.2f}")
#     print(f"   COGS:             ${cogs:>12,.2f}")
#     print(f"   Gross Profit:     ${gross_profit:>12,.2f}      ({gross_margin:.1%})")
#     print(f"   OPEX:             ${opex:>12,.2f}")
#     print(f"   EBIT:             ${ebit:>12,.2f}")
#     print(f"   TAX:              ${tax_amount:>12,.2f}")
#     print(f"   Net Profit:       ${net_profit:>12,.2f}      ({net_margin:.1%})")
#     print(f"   Verdict:          {verdict}")  # No need for :>12 just use space because :>12 looks good with numbers not text
#     print(f"{'='*40}\n")


# def main():
#     company, revenue, cogs, opex, tax_rate = get_inputs()  # Type in inputs

#     gross_profit, gross_margin, ebit, tax_amount, net_profit, net_margin = calculate(revenue, cogs, opex, tax_rate)  # Calculate

#     if net_margin > 0.20:
#         verdict = " Excellent "
#     elif net_margin > 0.10:
#         verdict = " Healthy "
#     elif net_margin > 0:
#         verdict = " Marginal "
#     else:
#         verdict = " At a Loss "

#     display(company, revenue, cogs, opex, gross_profit, gross_margin, ebit, tax_amount, net_profit, net_margin, verdict)


# main()
