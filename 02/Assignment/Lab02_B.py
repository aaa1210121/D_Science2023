#Lab02_B.py
from datetime import datetime,timedelta

def n_times_day(bday1, bday2, n):
    
    for i in range(100*365):
        c_date = bday2 + timedelta(days=i)
        d1 = (c_date - bday1).days
        d2 = (c_date - bday2).days
        if d1 == n*d2:
            result=(c_date.strftime('%Y-%m-%d %H:%M:%S'))
    return result


def main():
    now = datetime.now()
    print("Lab03 B-1")
    print(now)

    day_of_the_week = now.weekday()

    todays_date = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    print("Today's date and the day of the week:", todays_date[day_of_the_week])

    # TODO_B1

    # Your output should be like:
    # 2020-08-03 20:19:19.806211
    # Monday

    print("Lab03 B-2")
    s = input("Enter your birthday in mm/dd/yyyy format: ")  #'1/15/1997'
    format_string = "%m/%d/%Y "
    ur_birthday = datetime.strptime(s, "%m/%d/%Y")
    if now.month >= ur_birthday.month and now.day >= ur_birthday.day:
        next_birthday = datetime(now.year + 1, ur_birthday.month, ur_birthday.day)
        until_nextbirth = next_birthday - now
        print(until_nextbirth)
        print(now.year - ur_birthday.year) 
    else:
        next_birthday = datetime(now.year, ur_birthday.month, ur_birthday.day)
        until_nextbirth = next_birthday - now
        print(until_nextbirth)
        print(now.year - ur_birthday.year - 1)

    # TODO_B2
    # Your output should be like:
    # 280 days, 3:40:40.193789
    # 22
    print("Lab03 B-3")
    print("For people born on these dates:")
    bday1 = datetime(day=15, month=1, year=1997)
    bday2 = datetime(day=11, month=10, year=2003)

    print("Double Day is",n_times_day(bday1, bday2, n=2))
    # TODO_B3

    # Your output should be like:
    # 2020-01-01 00:00:00 (this is not the correct answer!)
    print("Lab03 B-4")
    print("Triple Day is ",n_times_day(bday1, bday2, n=3))

if __name__ == "__main__":
    main()