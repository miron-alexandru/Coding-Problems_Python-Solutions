# Problem Link: https://www.codewars.com/kata/585d7d5adb20cf33cb000235


# My Solution:
def find_uniq(arr):
    counter = {}
    for num in arr:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    for num in arr:
        if counter[num] == 1:
            return num
