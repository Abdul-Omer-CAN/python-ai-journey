# Calculator creation CS50P Lecture 1

x = float(input("What is you x value? "))  # we have to put int() or else python will treat it as a text and not a number
y = float((input("What is your y value? ")))  # int() for whole number input only OR float() which lets you do decimal points
z = round(x + y)  # you can also add int(x) + int(y)  &  add round() to round the answer
print(f"{z:,}")  # ":" this will tell that there are instruction next. "," comma in long no. ex 1,000


# OR


x = float(input("What is your x value sir "))
y = float(input("What is your y value sir? "))

m = round(x/y, 2)
print(m)
print(f"{m:.2f}")
