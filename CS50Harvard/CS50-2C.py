def main():
    x = int(input(" What is the x value? "))
    if is_even(x):
        print("EVEN")
    else:
        print("ODD")


# def is_even(n):
#     if n % 2 == 0:      # % sign means remainder - so the statement mean if the remainder is zero return true aka it is even.
#         return True     # Even numbers divided will have a remainder of zero
#     else:
#         return False    # We use return instead of print because that return value can be used in our main fxn but print cannot.

# OR

# More condensed form of def is_even

# def is_even(n):
#     return True if n % 2 == 0 else False

## Even more condenser version of def is_even(n) ##

def is_even(n):  # This is the simplest and cleanest way to write it!
    return n % 2 == 0


main()
