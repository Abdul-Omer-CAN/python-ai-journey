## Final Version of 4a exercise ##

def main():
    x = get_int("What is x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:   # will keep asking until the user inputs the right number
        try:
            return int(input(prompt))  # user inputs, then int checks whether its int, then true it return sends it to main()
        except ValueError:     # user types anything other than int except catches it and pass and loops fxn again.
            pass                  # will pass the value user input and loop it again w/out printing anything.


main()
