## Creating a file and adding names to it ##

# name = input("What is your name?")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")  # 'with' the file closes automatically when program is done being ran.


# with open

# # Reading a file ##

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")
