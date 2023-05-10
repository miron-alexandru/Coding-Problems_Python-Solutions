# Problem Link: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem


# Solution:
def minimumAbsoluteDifference(arr):
    # Sort the array
    arr.sort()
    min_diff = float("inf")

    # Iterate over the array and compare elements
    for i in range(1, len(arr)):
        diff = abs(arr[i] - arr[i - 1])
        if diff < min_diff:
            min_diff = diff

    return min_diff
