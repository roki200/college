import datetime

def cr_date(year, month, day):
    return datetime.datetime(year=year, month=month, day=day)

date = cr_date(2023, 6, 4)

print(date)
