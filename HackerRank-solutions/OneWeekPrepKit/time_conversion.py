# Problem Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem


# My Solution:
def timeConversion(s):
    # extract h, m, s
    hours, minutes, seconds = map(int, s[:-2].split(":"))
    period = s[-2:]
    if period == "AM":
        if hours == 12:
            hours = 0
    else:
        if hours != 12:
            hours += 12

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
