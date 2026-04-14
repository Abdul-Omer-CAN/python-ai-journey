name = input("What is your name? ")

match name:  # Match function smarter version of multiple if and elif functions. it takes name in our case and matches it against the cases below.
    case "Harry" | "Hermione" | "Ron":    # with '| ' you can add more variables in case
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:                                # with '_' you are basically telling anything not listed above will print(**Whatever you write**)
        print("Who?")

# In real life problems which are more complex and have more variables if/elif/else are gonna be used more. Match can only be used for checking
# one variable again the different cases. Match also cant handle >,<,<=,>=,and,or variables.
