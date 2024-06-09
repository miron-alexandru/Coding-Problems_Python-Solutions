# Problem Link: https://www.hackerrank.com/challenges/tower-breakers-1/problem


# My Solution:
def towerBreakers(n, m):
    if m == 1 or n % 2 == 0:
        return 2
    else:
        return 1
