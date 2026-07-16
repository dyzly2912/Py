import calendar

month, day, year = map(int, input().split())

week = calendar.weekday(year, month, day)

day = calendar.day_name[week]

print(day.upper())

