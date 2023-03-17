import re

def checkDate(day, month, year):
    # April, June, September, November = 30 days/ February = 28 days, unless leapyear so 29/ rest has 31 days
    month_dict = {4: 30, 6: 30, 9: 30, 11: 30, 2: 28}
    day_bound = month_dict.get(month, 31)

    # month is february
    if day_bound == 28:
        # checks if the year is a leap year
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    day_bound = 29
            else:
                day_bound = 29

    # if the day is in the range of possible days
    if day <= day_bound:
        return True
    return False

def isValidTimeStamp(str):
    date_regex = re.compile(r"([0-2]\d|3[01])-(0\d|1[0-2])-([12]\d{3})")
    match = date_regex.search(str)
    valid = False
    if match:
        day = int(match.group(1))
        month = int(match.group(2))
        year = int(match.group(3))
        valid = checkDate(day, month, year)

    return valid

def isValidColumn(column):
    if column != "mp10" and column != "mp25" and column != "o3" and column !="co" and column != "no2" and column != "so2":
        return False
    return True

def isValidMeasure(str):
    if not str.isnumeric():
        return False
    str = int(str)

    if str < 0: return False

    return True