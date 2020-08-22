import csv
import random
from datetime import datetime



""" #constant

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
        counter = counter + 1 """



# CONSTANT
FILENAME = 'writing_csv.csv'
COLUMN_NAMES = ['employee_id', 'entered_at', 'enter_for']
MAX_NUMBER_LOGS = 10000
# FUNCTION
def fake_enter_for():
    enter_for_list = ['suppliement', 'reports', 'meeting', 'payment', 'bathroom', 'call', 'lunch']
    return random.choice(enter_for_list)




def fake_employee_id():
    employee_id_list = [1002, 5000, 34123, 54504, 606506, 10203, 540604, 1231235, 123123123, 10]
    return random.choice(employee_id_list)   

def fake_timestamp():
    now = datetime.now()
    now = now.replace(hour= random.randint(7,18), minute= random.randint(0,59))
    ts = datetime.timestamp(now)
    return int(ts)




with open(FILENAME, mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=COLUMN_NAMES)

    # WRITING HEADERS
    writer.writeheader()
    counter = 1
    while counter <= MAX_NUMBER_LOGS:
        writer.writerow({
            'employee_id': fake_employee_id(),
            'entered_at': fake_timestamp(),
            'enter_for': fake_enter_for()
        })
        counter += 1