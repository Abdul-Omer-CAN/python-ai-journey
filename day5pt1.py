import csv

with open("portfolio.csv", "r") as file:   # "r" means open for read | "w" means open for writing to file | "a" means open for adding to the file
    reader = csv.reader(file)   # reads each line individually or else python will read it as one big block.
    next(reader)  # Skip the first row aka header row so that python does not try to process header.
    for row in reader:
        ticker = row[0]
        price = float(row[1])
        quantity = int(row[2])
        value = price * quantity
        print(f"{ticker}: ${value:,.2f}")


with open("report.csv", "w", newline="") as file:           # now we are creating a new file called report.csv
    writer = csv.writer(file)                               # creater writer object
    writer.writerow(["Ticker", "Price", "Quantity", "Total Value"])  # writing the first row - adding headers
    with open("portfolio.csv", "r") as portfolio:  # opens our portfolio.csv(the old one we created) for reading
        reader = csv.reader(portfolio)   # creates a reader that goes through portfolio.csv row by row
        next(reader)  # skips the header row in the portoflio.csv file
        for row in reader:  # now we are looping through each stock row.
            ticker = row[0]   # out ticker will be row 0 in portfolio.csv and foorsooth
            price = float(row[1])
            quantity = int(row[2])
            value = price*quantity
            writer.writerow([ticker, f"{price:.2f}", quantity, f"{value:.2f}"])   # Writes one row for each stock in our new report.csv

print(("Read saved to report.csv"))  # Always open existing .csv files with 'r' and then you can 'w' or 'a' or else your old data might be deleted.


#  day 5 list of new CSV functions: | csv.reader(file) -> reads csv row by row
#  csv.writer(file) -> writes to csv file
#  writer.writerow([]) -> writes a row to csv
#  writer. write rows([]) -> writes multiples rows to csv
#  next(reader) -> skips the row (header)
#  "r" is for read only | "w" is for write only | "a" is for adding to an existing files
#  with open("file.csv", "r or w or a") as file -> open file for r or w or a
