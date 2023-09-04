import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(f"(\d*):?(\d*)? ([AP]M) to (\d*):?(\d*)? ([AP]M)",s):
        start_hour, start_minute, start_ampm, end_hour, end_minute, end_ampm = matches.groups()
        start_hour = int(start_hour)
        start_minute = int(start_minute) if start_minute else 0
        end_hour = int(end_hour)
        end_minute = int(end_minute) if end_minute else 0
        if (start_hour == 12 and start_ampm == "AM"):
            start_hour -= 12
        if start_ampm == "PM" and start_hour != 12:
            start_hour += 12
        if end_ampm == "PM" and end_hour != 12:
            end_hour += 12
        if start_minute >= 60 or end_minute >= 60:
            raise ValueError
        return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()