months = ["January",
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
    "December"]
def formatDate(date):
    date = date.strip()
    if "/" in date:
        date = date.split("/")
        try:
            day = date[1]
            month = date[0]
            if int(day) > 31:
                main()
            if int(month) > 12:
                main()
        except ValueError:
            main()
        #YYYY-MM-DD
        return print(f"{date[2]}-{month.zfill(2)}-{day.zfill(2)}")
    elif "," in date:
        date = date.split(",")
        month_day = date[0].split()
        if month_day[0] in months:
            month_ = str(months.index(month_day[0])+1)
            day = month_day[1]
            if int(day) > 31:
                main()
            print(f"{date[1]}-{month_.zfill(2)}-{str(day).zfill(2)}")
        else:
            main()
    else:
        main()
def main():
    date = getDate("Date input: ")
    return formatDate(date)
def getDate(date_input):
    return str(input(date_input))
main()