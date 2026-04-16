# print("meow\n"*3, end="")  # end="" removes the last space line. without it there is an empty line after the last meow

# OR

# for i in range(3):
#     print("meow")

# OR

# i = 0
# while i < 3:
#     print("meow")
#     i += 1

### New exercise ####

# while True:
#     n = int(input("What is your 'n'? "))
#     if n > 0:
#         break
# for _ in range(n):
#     print("meow3")


#### New exercise def function ####

def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What is you n? "))
        if n > 0:
            break
    return n


def meow(n):
    for x in range(n):
        print("meow")


main()
