# def main():
#     print_column(3)


# def print_column(height):      # height can be called x or y or whatever. Just for mario game example's sake we using height.
#     print("#\n" * height, end=(""))


# main()


######## Last exercise #########

def main():
    print_square(3)


def print_row(width):   # this will generate #*3= ###
    print("#" * width)


def print_square(size):         # This will make th size by using our range which is 3 and multiplying "###"*3 aka print_row *3
    for i in range(size):
        print_row(size)


main()
