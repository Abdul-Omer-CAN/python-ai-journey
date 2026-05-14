import csv

name = input("Whats your name? ")
home = input("Where is your home? ")

with open("student3.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"home": home, "name": name})
s
