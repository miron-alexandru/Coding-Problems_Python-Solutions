# problem link: https://www.hackerrank.com/challenges/quicksort1/problem


# my solution:
def quickSort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    # pivot
    p = arr[0]

    # initialize left and right subarrays
    left, middle, right = [], [], []

    # partition the array
    for num in arr:
        if num < p:
            left.append(num)
        elif num > p:
            right.append(num)
        else:
            middle.append(num)

    # recursively sort left and right subarrays
    left = quickSort(left)
    right = quickSort(right)

    # concatenate the sorted subarrays and pivot
    return left + middle + right
