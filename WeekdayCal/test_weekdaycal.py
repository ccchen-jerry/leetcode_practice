import random
import datetime, calendar
from weekdaycal import day_of_week

def test_date():
    for i in range(10):
        random_day = datetime.date.fromtimestamp(random.randint(1, 1000000000))
        print(str(random_day))
        assert day_of_week(random_day.year, random_day.month, random_day.day) == calendar.day_name[random_day.weekday()]


