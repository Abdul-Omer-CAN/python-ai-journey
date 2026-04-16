# students = ["Hermione", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i + 1, students[i])   # the reason why we put [i] in students is to pick each variable individually.
# # e.g.  student[0] = Hermione | student [1] = Harry

##### New exercise on creating dictionaries aka dict #########

# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }

# for student in students:
#     print(student, students[student], sep=", ")

### New exercise but more variables ###

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronas": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronas": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronas": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronas": None}
]

# 'key=' tells python to sort it by whatever you want it to
# 'lambda' i just a function instead of writing def () aka lambda [input] -> lambda [ouput]. Output is name in our case
for student in sorted(students, key=lambda student: student["name"]):
    print(student["name"], student["house"], student["patronas"], sep=", ")
