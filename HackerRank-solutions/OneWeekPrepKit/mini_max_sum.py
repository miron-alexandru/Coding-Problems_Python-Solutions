# Problem Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem


# My Solution:
# O(n) time complexity
def miniMaxSum(arr):
    min_val = max_val = arr[0]
    total_sum = arr[0]
    for i in range(1, len(arr)):
        min_val = min(min_val, arr[i])
        max_val = max(max_val, arr[i])
        total_sum += arr[i]
    print(total_sum - max_val, total_sum - min_val)

# O(n log n)
def miniMaxSum(arr):
    arr = sorted(arr)
    print(sum(arr[:4]), sum(arr[1:]))