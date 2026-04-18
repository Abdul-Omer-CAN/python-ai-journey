# Loan Eligibility Checker

name = input("Applicant's name: ")  # Our Input ####
salary = float(input(("Annual Salary ($): ")))
credit_score = int(input("Credit score: "))
loan_amount = float(input("Loan amount requested ($): "))
loan_term = int(input("Loan term (years): "))


# Calculations

debt_ratio = loan_amount / salary  # Process ###
monthly_payment = loan_amount / (loan_term*12)


# Determining Elgibility

if credit_score >= 750 and debt_ratio <= 3:  # More processes ##
    verdict = "Approved"
    interest_rate = 0.05
elif credit_score >= 700 and debt_ratio <= 4:
    verdict = "Conditionally Approved"
    interest_rate = 0.07
elif credit_score >= 650 and debt_ratio <= 5:
    verdict = "Approved with higher rate"
    interest_rate = 0.10
else:
    verdict = "Denied"
    interest_rate = 0


# Output report

# print(f"\n{'='*45}")
# print("     Loan Application Report     ")
# print(f"{'='*45}")
# print(f" Applicant:           {name}")
# print(f" Loan Amount:         ${loan_amount:>12,.2f}")   # lines up the decimal points :>12
# print(f" Annual Salary:       ${salary:>12,.2f}")
# print(f" Credit Score:        {credit_score:>12}")    # no need for :>12 because credit score has no decimal points
# print(f" Debt Ratio:          {debt_ratio:.1f}x  ")
# print(f" Loan Term:           {loan_term} Years ")
# print(f"{'='*45}")
# print(f" Interest Rate:       {interest_rate:.1%}")
# print(f" Monthly Payment:     ${monthly_payment:>12,.2f}")  # .2f means 2 decimal places for ex. .2f
# print(f" Decision:            {verdict}")
# print(f"{'='*45}\n")

## Modified for Proper Alignment ##
print(f"\n{'='*45}")
print("     Loan Application Report     ")
print(f"{'='*45}")
print(f" Applicant:           {name}")
print(f" Loan Amount:         ${loan_amount:>12,.2f}")   # lines up the decimal points :>12
print(f" Annual Salary:       ${salary:>12,.2f}")
print(f" Credit Score:        {credit_score:>13}")    # no need for :>12 because credit score has no decimal points
print(f" Debt Ratio:          {debt_ratio:>12.1f}x")
print(f" Loan Term:           {str(loan_term) + ' years':>12}")  # with str() you can add numbers with texts like we did with 'year'
print(f"{'='*45}")
if verdict == "Denied":
    print(f" Interest Rate:  {'N/A':>12}")
else:
    print(f" Interest Rate:   {interest_rate:.1%}")
print(f" Monthly Payment:     ${monthly_payment:>12,.2f}")  # .2f means 2 decimal places for ex. .2f
print(f" Decision:            {verdict}")
print(f"{'='*45}\n")
