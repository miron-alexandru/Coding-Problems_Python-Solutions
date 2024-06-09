# problem link: https://www.hackerrank.com/challenges/countingsort2/problem


# my solution:
def countingSort(arr):
    # find the maximum value in the input list
    max_val = max(arr)

    count = [0] * (max_val + 1)

    # traverse the input list and increment count for each value
    for val in arr:
        count[val] += 1

    # traverse the count array and output each value that number of times
    sorted_arr = []
    for val in range(max_val + 1):
        for _ in range(count[val]):
            sorted_arr.append(val)

    return sorted_arr
