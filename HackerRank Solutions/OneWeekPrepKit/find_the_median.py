# Problem: https://www.hackerrank.com/challenges/find-the-median/problem


# My solution:
def findMedian(arr):
    arr.sort()
    n = len(arr)

    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) // 2
