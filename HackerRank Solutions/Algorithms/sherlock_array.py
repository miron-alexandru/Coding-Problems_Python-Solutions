# Problem Link: https://www.hackerrank.com/challenges/sherlock-and-array/problem


# My Solution:
def balancedSums(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i in arr:
        if left_sum == total_sum - left_sum - i:
            return "YES"
        left_sum += i
    return "NO"
