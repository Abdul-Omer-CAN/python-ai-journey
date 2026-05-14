students = []

with open("student.csv") as file:
    for line in file:
        if "," in line:
            name, house = line.rstrip().split(",")
            student = {"name": name, "house": house}
            students.append(student)


for student in sorted(students, key=lambda student: student["name"]):   # whatever 'key ='  sort it by that. in our case by house name alphabetically. reverse is opposite alphabetical order.
    print(f"{student['name']} is in {student['house']}")    # lambda is a quick use fxn instead of using def ... 'lambda input: output'
# lambda in our case take student and return student["name"]
