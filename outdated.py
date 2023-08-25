import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

months_dict = months = {
    "January" : "01",
    "February" : "02",
    "March" : "03",
    "April" : "04",
    "May" : "05",
    "June" : "06",
    "July" : "07",
    "August" : "08",
    "September" : "09",
    "October" : "10",
    "November" : "11",
    "December" : "12"
}

def main():
    inp_date = input("Date: ").strip()
    if validity(inp_date):
        print(out_date(inp_date))

def validity(inp):
    # MAKE SEPERATORS SIMILAR IF NOT
    # CHECK IF THE MONTH IS WITHIN LIST OR IS LESS THAN 13
    # CHECK IF THE DAY IS LESS THAN 31
    # CHECK IF YEAR IS 4 DIGITS
    if re.match("[0-1]?[1-9]/[0-3]?[0-9]/[0-9]{4}$",inp):
        t_dt = inp.split("/")
        if int(t_dt[1]) > 31 or int(t_dt[1]) < 1:
            #print("failed")
            main()
        else:
            #print("part1")
            return True
    elif "," in inp or " " in inp:
        for month in months:
            if month in inp.title():

                inp = inp.replace(" ",",")
                inp = inp.replace(",,",",")
                new_inp = inp.split(",")
                new_inp[0] = new_inp[0].title()
                #print(new_inp)
                if new_inp[0] not in months:
                    main()
                else:
                     if int(new_inp[1]) > 31 or int(new_inp[1]) < 1:
                        main()
                     else:
                         return True
            else:
                pass

    else:
        #print("failed-2nd")
        main()

def out_date(inp):
    # use the above regex to provide new values
    if re.match("[0-1]?[1-9]/[0-3]?[0-9]/[0-9]{4}$",inp):
        #print("part1.1")
        t_dt = inp.split("/")
        if len(t_dt[1]) == 1:
            t_dt[1] = "0"+t_dt[1]
        if len(t_dt[0]) == 1:
            t_dt[0] = "0"+t_dt[0]
        out = str(t_dt[2]+"/"+t_dt[0]+"/"+t_dt[1])
        return out
    else:
        #print("part2.1")
        inp = inp.replace(" ",",")
        inp = inp.replace(",,",",")
        new_inp = inp.split(",")
        new_inp[0] = new_inp[0].title()
        new_inp[0] = months_dict[new_inp[0]]
        if len(new_inp[1]) == 1:
            new_inp[1] = "0"+new_inp[1]
        out = str(new_inp[2]+"/"+new_inp[0]+"/"+new_inp[1])
        return out

if __name__ == "__main__":
    main()