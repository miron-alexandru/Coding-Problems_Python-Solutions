# Problem Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem


# My Solution:
def diagonalDifference(arr):
    n = len(arr)
    left_sum = 0
    right_sum = 0

    for i in range(n):
        left_sum += arr[i][i]
        right_sum += arr[i][n - 1 - i]
    return abs(left_sum - right_sum)
