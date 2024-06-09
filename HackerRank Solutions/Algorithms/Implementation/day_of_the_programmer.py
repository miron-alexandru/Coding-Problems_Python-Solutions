# problem link: https://www.hackerrank.com/challenges/day-of-the-programmer/problem


# my solution:
def dayOfProgrammer(year):
    if year < 1918:
        leap = year % 4 == 0
    elif year == 1918:
        return "26.09.1918"
    else:
        leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    if leap:
        return "12.09.%04d" % year
    else:
        return "13.09.%04d" % year
