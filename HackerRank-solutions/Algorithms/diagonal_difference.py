# Problem Link: https://www.hackerrank.com/challenges/diagonal-difference/problem


# My Solution:
def diagonalDifference(arr):
    n = len(arr)
    sum_primary = 0
    sum_secondary = 0
    for i in range(n):
        sum_primary += arr[i][i]
        sum_secondary += arr[i][n-i-1]
        
    return abs(sum_primary - sum_secondary)
