# try:
#     x = int(input("What is your x? "))
# except:
#     print("x is not an integer!")
# else:
#     print(f"x is {x}")

# ^ nothing new here just try/except/else pair


## Better way of doing this ###
while True:
    try:
        x = int(input("What is your x? "))

    except:
        print("x is not an integer!")

    else:
        break

print(f"x is {x}")

# Added while True and else to break and then it prints x if it is an integer. if not it will keep until you input an integer.
# without break it would keep keep looping and asking even if you enter a number.
