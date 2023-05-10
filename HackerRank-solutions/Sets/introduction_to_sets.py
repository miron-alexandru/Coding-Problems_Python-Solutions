"""
Ms. Gabriel Williams is a botany professor at District College.
One day, she asked her student Mickey to compute
the average of all the plants with distinct heights in her greenhouse.


Formula Used:
Average = sum of distinct heights / total number of distinct heights


Returns
float: the resulting float value rounded to 3 places after the decimal


Input format
The first lien contains the integer, n. the size of arr.
The second line contains the N space separated integers, arr[i]


Sample input
10
161 182 161 154 176 170 167 171 170 174


Sample output
169.375
"""


# Solution 1:
def average(array):
    array = set(array)
    return round(sum(array) / len(array), 3)


# Solution 2
def average(arr):
    array = set(arr)
    heights_sum = sum(height for height in array)
    average = heights_sum / len(array)
    return average


# Solution 3
# Better space complexity
def average(array):
    heights = {}
    total = 0
    for height in array:
        if height not in heights:
            heights[height] = True
            total += height
    return round(total / len(heights), 3)
