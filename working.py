import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    hours = [1,2,3,4,5,6,7,8,9,10,11,12]
    mins = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]
    if re.match("[0-9]?[0-9](:[0-9][0-9])? (AM|PM) to [0-9]?[0-9](:[0-9][0-9])? (AM|PM)",s):
        # SPLIT BY SPACE
        time_list = re.split(" ",s)
        from_time = time_list[0]
        from_ampm = time_list[1]
        to_time = time_list[-2]
        to_ampm = time_list[-1]
        # FIND OUT IF TIMES GIVEN ARE HAVING :
        # FIND OUT IF TIMES ARE VALID
        # IF FROM OR TO IS PM ADD 12 TO HOURS
        if ":" in from_time:
            from_time_broken = from_time.split(":")
            from_hh = from_time_broken[0]
            from_mm = from_time_broken[1]
            if int(from_hh) not in hours or int(from_mm) not in mins:
                print("Fail")
                raise ValueError
            else:
                if from_ampm == "PM":
                    from_hh = int(from_hh)+12
                    #print(f"from time is {from_hh:02}:{int(from_mm):02}")
                    new_from_time = "".join(str(f"{from_hh:02}:{int(from_mm):02}"))
                else:
                    #print(f"from time is {int(from_hh):02}:{int(from_mm):02}")
                    new_from_time = "".join(str(f"{int(from_hh):02}:{int(from_mm):02}"))
        else:
            from_hh = int(from_time)
            if from_hh in hours:
                if from_ampm == "PM":
                    from_hh = from_hh+12
                    #print(f"from time is {from_hh:02}:00")
                    new_from_time = "".join(str(f"{from_hh:02}:00"))
                else:
                    #print(f"from time is {from_hh:02}:00")
                    new_from_time = "".join(str(f"{from_hh:02}:00"))
            else:
                #print("Fail")
                raise ValueError
        if ":" in to_time:
            to_time_broken = to_time.split(":")
            to_hh = to_time_broken[0]
            to_mm = to_time_broken[1]
            if int(to_hh) not in hours or int(to_mm) not in mins:
                #print("Fail")
                raise ValueError
            else:
                if to_ampm == "PM":
                    to_hh = int(to_hh)+12
                    #print(f"to time is {to_hh:02}:{int(to_mm):02}")
                    new_to_time = "".join(str(f"{to_hh:02}:{int(to_mm):02}"))
                else:
                    #print(f"to time is {int(to_hh):02}:{int(to_mm):02}")
                    new_to_time = "".join(str(f"{int(to_hh):02}:{int(to_mm):02}"))
        else:
            to_hh = int(to_time)
            if to_hh in hours:
                if to_ampm == "PM":
                    to_hh = to_hh+12
                    #print(f"to time is {to_hh:02}:00")
                    new_to_time = "".join(str(f"{to_hh:02}:00"))
                else:
                    #print(f"from time is {to_hh:02}:00")
                    new_to_time = "".join(str(f"{to_hh:02}:00"))
            else:
                #print("Fail")
                raise ValueError
        new_time = "".join(new_from_time+" to "+new_to_time)
        return new_time
    else:
        raise ValueError

if __name__ == "__main__":
    main()