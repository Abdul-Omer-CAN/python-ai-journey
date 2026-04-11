# Steps of writing a program

credit_score = int(input("Credit Score: "))


if credit_score >= 750:
    rating = "Excellent"
elif credit_score >= 700:
    rating = "Good"
elif credit_score >= 650:
    rating = "Fair"
elif credit_score >= 600:
    rating = "Poor"
else:
    rating = "Very Poor"

print(f"Credit rating: {rating}")


# 1st step is Imports ONLY if you are importing anything from an external library (Not here)
# 2nd Step  We started with Input where we ask the user for data using "name=and the arguments"
# 3rd Step is our Processes OR Calculations before processes(do something with the data)
# 4th Step is output which is print() function for example.
