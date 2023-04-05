# problem link: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem


# my solution:
def beautifulDays(i, j, k):
    count = 0
    for day in range(i, j+1):
        reversed_day = int(str(day)[::-1])
        if abs(day - reversed_day) % k == 0:
            count += 1
    return count
