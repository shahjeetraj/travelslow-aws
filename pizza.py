import sys
import os
from tabulate import tabulate
import csv

def main():
    if len(sys.argv) == 1:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not os.path.exists(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)
    else:
        table = get_data_from_csv(sys.argv[1])
        print(tabulate(table,tablefmt="grid"))

def get_data_from_csv(csv_file):
    with open(csv_file) as csvfile:
        return list(csv.reader(csvfile, delimiter=','))

if __name__ == "__main__":
    main()