'''
Using Zeller's congruence


'''

Zeller_WEEKDAY = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def day_of_week(year:int, month:int, day:int):    
    #converting starting month of the year
    if month < 3:
        month += 12
        year -= 1
    
    #creating necessary variables
    centry = year // 100

    weekdaynum = (day + (13 * (month + 1)) // 5 + year + year // 4 - year // 100 + year // 400) % 7

    return Zeller_WEEKDAY[weekdaynum]
