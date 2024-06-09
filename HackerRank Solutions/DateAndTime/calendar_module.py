# Problem link: https://www.hackerrank.com/challenges/calendar-module/problem


# My solution:
# Without calendar module.

import datetime

m, d, y = map(int, input().split())
answer = datetime.date(y, m, d)
print(answer.strftime("%A").upper())


# With calendar module
import datetime
import calendar

m, d, y = map(int, input().split())
answer = datetime.date(y, m, d)
print(calendar.day_name[answer.weekday()].upper())
