# problem link: https://www.hackerrank.com/challenges/drawing-book/problem


# my solution:
def pageCount(n, p):
    beginning = p // 2
    end = (n // 2) - (p // 2)
    return min(beginning, end)