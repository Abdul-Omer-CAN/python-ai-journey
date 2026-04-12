####### In this Section we learn - def, parameters and return values ######

# def greet(name, account_type):   # name is our placeholder where it gets replaced w/ whatever we put in greet when calling that function
#     print(f"Hello {name}, welcome to your {account_type} account!")


# greet("Abdulrehman", 'Premium')
# greet("Sarah", 'Standard')
# greet("Abdulraheem", 'World Elite')

################# NEW EXERCISE #######################

# def calculate_interest(principal, rate, years):   # these are parameters ex principal , rate, years. parameters aka placeholders
#     total = principal * (1+rate) ** years
#     return total


# result1 = calculate_interest(10000, 0.07, 5)       # these are arguments 1000 or 0.07 or 5 . arguments aka actual values
# result2 = calculate_interest(50000, 0.05, 10)
# result3 = calculate_interest(100000, 0.10, 20)


# print(f"Investment 1: ${result1:,.2f}")
# print(f"Investment 2: ${result2:,.2f}")
# print(f"Investment 3: ${result3:,.2f}")

######################## Creating the Interest comparison tool ##################################


def calculate_interest(principal, rate, years):  # Formatting of a program -> Function goes first
    total = principal * (1 + rate) ** years
    return total


principal = float(input("Inital investment ($): "))  # -> Input goes next
rate1 = float(input("Rate 1 (e.g. 0.05 for 5%): "))
rate2 = float(input("Rate 2 (e.g. 0.07 for 7%): "))
rate3 = float(input("Rate 3 (e.g. 0.10 for 10%): "))
years = int(input("Investment period (years): "))


result1 = calculate_interest(principal, rate1, years)
result2 = calculate_interest(principal, rate2, years)
result3 = calculate_interest(principal, rate3, years)
best = max(result1, result2, result3)


print(f"\n{'='*50}")                           # for the line below remember to always use {} with "" when you want to add :>12 or :^ 50
print(f" {'COMPOUND INTEREST COMPARISON':^50}")  # This centers the title in a 50 character wide border
print(f"{'='*50}")
print(f"Initial Investment:   ${principal:>12,.2f}")
print(f"Period:               {years} years")
print(f"{'='*50}")
print(f"  Rate 1 ({rate1:.1%}):          ${result1:>12,.2f}")
print(f"  Rate 2 ({rate2:.1%}):          ${result2:>12,.2f}")
print(f"  Rate 3 ({rate3:.1%}):          ${result3:>12,.2f}")
print(f"{'='*50}")
print(f"  Best Return:            ${best:>12,.2f}")
print(f"{'='*50}\n")
