salary = int(input("Annual Salary($): "))
credit_score = int(input("Credit Score: "))

if salary >= 30000 and credit_score >= 700:
    print("Approved")

elif salary >= 50000 or credit_score >= 750:
    print("Conditionally Approved")

else:
    print("Denied")
