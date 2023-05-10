# problem link: https://www.hackerrank.com/challenges/array-left-rotation/problem


# my solution:
def rotateLeft(d, arr):
    n = len(arr)
    # case where d >= n
    d = d % n
    return arr[d:] + arr[:d]
