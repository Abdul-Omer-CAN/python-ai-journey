def hello():
    return ("Hello")  # use return() if you use print() it will generate none


name = input("What is your name ser? ")
print(hello(), end="")
print(" " + name)

print(hello(), name)  # another way easier  instead of doing line 6 and 7

# Second lesson


def hello(to="World"):
    print("hello, ", to)  # "to" holds the word "world" think of to as a holder of a word you specify it to hold


hello()
name = input("What's your name? ")
hello(name)


# Third lesson creating 2 functions

def main():
    name = (input("What is your name? "))
    hello()


def hello(to="world"):
    print("hello,", to)


main()


# Last lesson

def main():
    x = int(input("What is your x value ser? "))
    print("x squared is", square(x))


def square(x):
    return (x*x)  # or you can also write the code as return (pow(n,2)) means to the power of 2


main()
