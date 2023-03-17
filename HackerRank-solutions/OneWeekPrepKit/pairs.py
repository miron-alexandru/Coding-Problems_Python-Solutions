# problem link: https://www.hackerrank.com/challenges/pairs/problem


# My Solution:
def pairs(k, arr):
    # create set to store values
    values = set(arr)

    count = 0
    
    for value in arr:
        # Check if the value + k is in the set
        if value + k in values:
            count += 1

    return count