import re
import sys
import inflect
from datetime import date
p = inflect.engine()

def main():
    date_of_birth = input("Date of Birth: ")
    try:
        year, month, day = check_date(date_of_birth)
        valid_dob = date(int(year),int(month),int(day))
    except:
        sys.exit("Invalid Date")
    date_today = date.today()
    diff = date_today - valid_dob
    mins = diff.days * 24 * 60
    print(f"{p.number_to_words(mins).capitalize()} minutes")


def check_date(d):
    if re.match("^[1-9][0-9]{3}-[0-1][0-9]-[0-3][0-9]",d):
        year, month, day = d.split("-")
        return year, month, day
    #else:
        #sys.exit("Invalid Date")

if __name__ == "__main__":
    main()