# problem link: https://www.hackerrank.com/challenges/circular-array-rotation/problem


# my solution:
def circularArrayRotation(a, k, queries):
    n = len(a)
    # cases where k > n
    k = k % n
    # perform right circular rotation
    a = a[-k:] + a[:-k]
    # return elements at the query indices
    return [a[q] for q in queries] 