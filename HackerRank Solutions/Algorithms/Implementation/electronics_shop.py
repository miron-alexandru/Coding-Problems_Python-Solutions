# problem link: https://www.hackerrank.com/challenges/electronics-shop/problem


# my solution::
def getMoneySpent(keyboards, drives, b):
    max_cost = -1
    for k in keyboards:
        for d in drives:
            cost = k + d
            if cost <= b and cost > max_cost:
                max_cost = cost
    return max_cost
