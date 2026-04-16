name = input("Whats your name? ").strip().capitalize()  # strip removed unneccessary space and capitalize() caps the first letter of the input
print(f" Hello, {name}")  # {} to add input from another variable/function

# OR


name2 = input("What is your name? ")
print("Hello, ", end="")  # adding end="" basically merges that line and the next
print(name2)


# How to use sep=''

name2 = input("What is your name? ")
print("Hello, ", name2, sep='--')  # adding sep="" basically adds seperation w/ the character in ''


# usage of / lets us use "" twice without giving syntax error aka escaping

print("Hello, \"friend\"")

# remember is you want to pull a variable or value using {} you have to use f" to enable the proper formatting
# if you use .replace"."."" it will remove all periods in the input you can add this if you want after .capitalize in the first line of code
# You can use .title"" to make it like a title - can be added to line one

# Split user's name into first and last name using .split(" ")
# first, last = name.split(" ")

name = input("Customer's name ").strip().title()
first, last = name.split(" ")  # strip is used here () to seperate first and last name
print(f"hello, {first}")
