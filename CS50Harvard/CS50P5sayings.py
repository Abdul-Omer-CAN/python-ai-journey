def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


if __name__ == "__main__":       # using this the main() will only run if called by this .py file if say.py file calls it it wont run
    main()                       # without __name__ it will run both .py files and print world and your name on the cs50psay.py file too.
