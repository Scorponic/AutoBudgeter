import os
import csv

csv_dir = "../../Budget/Dec_2022" # Hard coded, look for .csv here
category_file = "category_mapping.csv"

categories = {}
totals = {"all": 0}


def main():
    setup()

    csv_file_list = os.listdir(csv_dir)

    for name in csv_file_list:
        processCSV(name)

    print(totals)


def setup():
    # read in category mapping as dictionary from .csv
    # set up totals dictionary from categories in mapping
    with open(category_file, "r") as f:
        reader = csv.reader(f)

        for row in reader:
            categories[row[0]] = row[1]

            if row[1] not in totals:
                totals[row[1]] = 0


def processCSV(name):
    csv_file = os.path.join(csv_dir, name)

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            processEntry(row)


def processEntry(entry):
    value = 0

    category = getCategory(entry["Description"])

    if entry["Debit"] != "":
        value += float(entry["Debit"])
    else:
        value += float(entry["Credit"])

    totals[category] += value


def getCategory(name):
    for keyword in categories:
        if keyword.lower() in name.lower():
            return categories[keyword]
    return "all"


if __name__ == "__main__":
    main()
