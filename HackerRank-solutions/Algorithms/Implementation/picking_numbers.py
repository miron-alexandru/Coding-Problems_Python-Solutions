# problem link: https://www.hackerrank.com/challenges/picking-numbers/problem


# my solution:
def pickingNumbers(a):
    max_length = 0
    for i in set(a):
        count_i = a.count(i)
        count_j = a.count(i + 1)
        max_length = max(max_length, count_i + count_j)
    return max_length
