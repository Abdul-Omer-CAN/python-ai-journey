with open("student.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        if len(row) > 1:          # if there is more than one item in the row then print it if not then dont print it. items are seperated by ','
            print(f"{row[0]} is in {row[1]}")
