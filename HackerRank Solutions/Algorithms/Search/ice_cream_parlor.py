# Problem Link: https://www.hackerrank.com/challenges/icecream-parlor/problem


# My Solution:
def icecreamParlor(m, arr):
    cost_dict = {}
    for i in range(len(arr)):
        if arr[i] in cost_dict:
            return sorted([cost_dict[arr[i]], i + 1])
        cost_dict[m - arr[i]] = i + 1
    return []
