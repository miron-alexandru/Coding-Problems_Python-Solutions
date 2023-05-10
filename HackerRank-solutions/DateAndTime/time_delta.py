# Problem Link: https://www.hackerrank.com/challenges/python-time-delta/problem


# My Solution:
from datetime import datetime


def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    delta = abs(int((dt1 - dt2).total_seconds()))
    return delta


if __name__ == "__main__":
    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)
