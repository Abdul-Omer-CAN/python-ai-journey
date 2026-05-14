import csv

students = []

with open("student2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):  # the key=lambda.. i saying basically 'for each student use their name to sort.
    print(f"{student['name']} is from {student['home']}")
