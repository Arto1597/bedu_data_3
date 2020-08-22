import csv


# crear una constante "file_name"
FILENAME = 'employees.csv'
with open(FILENAME) as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)
    