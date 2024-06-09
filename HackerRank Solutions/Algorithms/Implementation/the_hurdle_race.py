# Problem Link: https://www.hackerrank.com/challenges/the-hurdle-race/problem

# My Solution:


def hurdleRace(k, height):
    max_height = max(height)
    diff = max_height - k
    if diff < 0:
        return 0
    else:
        return math.ceil(diff)
