# Problem Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/problem


# My Solution:
def countingSort(arr):
    counts = [0] * 100
    for i in arr:
        counts[i] += 1
    return counts
