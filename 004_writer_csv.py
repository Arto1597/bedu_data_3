import csv




#constant

FILENAME = "writing_csv.csv"
COLUMNS_NAMES = ["employees_id", "entered_at", "enter_for"]
MAX_NUMBER_LOGS = 100

with open(FILENAME, mode= "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=COLUMNS_NAMES)



    #Writng Headers
    writer.writeheader()
    counter = 1

    while counter <= MAX_NUMBER_LOGS:
        writer.writerow({
            "employees_id": 1002,
            "entered_at": 53145134532,
            "enter_for": "LUNCH"
        })
        counter = counter + 1

# CONSTANT
FILENAME = 'writing_csv.csv'
COLUMN_NAMES = ['employee_id', 'entered_at', 'enter_for']
MAX_NUMBER_LOGS = 100

with open(FILENAME, mode='w', newline= '') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=COLUMN_NAMES)
    
    # WRITING HEADERS
    writer.writeheader()
    counter = 1
    while counter <= MAX_NUMBER_LOGS:
        writer.writerow({
            'employee_id': 1002,
            'entered_at': 716253576253,
            'enter_for': 'LUNCH'
        })
        counter += 1