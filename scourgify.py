import csv
import os
import sys

# CREATE A MAIN FUNCTION THAT WILL CHECK INPUT AND THEN READ & WRITE FILE
def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not os.path.exists(sys.argv[1]):
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)
    else:
        transform_file(sys.argv[1],sys.argv[2])
        sys.exit()

def transform_file(before_file,after_file):
    students_data = []
    with open(before_file) as file1:
        for row in csv.DictReader(file1):
            students_data.append({"first": row["name"].split(", ")[1],"last": row["name"].split(", ")[0],"house":row["house"] })

    with open(after_file, "w") as file2:
        writer = csv.DictWriter(file2, fieldnames=["first","last","house"])
        writer.writerow({"first":"first","last":"last","house":"house"})
        for i in range(len(students_data)):
            first = students_data[i]["first"]
            last = students_data[i]["last"]
            house = students_data[i]["house"]
            writer.writerow({"first":first,"last":last,"house":house})


if __name__ == "__main__":
    main()