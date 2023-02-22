# Problem Link: https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c


# My Solution:

def max_sequence(arr):
    if not arr:
        return 0

    max_ending_here = max_so_far = 0
    for num in arr:
        max_ending_here = max(0, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
