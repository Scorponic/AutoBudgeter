import os
import csv

csv_dir = "../../Budget/Dec_2022" # Hard coded, look for .csv here

totals = {"all": 0}

def main():
    print("test")    
    csv_file_list = os.listdir(csv_dir)

    for name in csv_file_list:
        processCSV(name)

    print(totals)


def processCSV(name):
    csv_file = os.path.join(csv_dir, name)

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            processEntry(row)

def processEntry(entry):
    value = 0
    
    if entry["Debit"] != "":
        value += float(entry["Debit"])
    else:
        value += float(entry["Credit"])

    totals["all"] += value



if __name__ == "__main__":
    main()
