# problem link: https://www.hackerrank.com/challenges/beautiful-triplets/problem


# my solution:
def beautifulTriplets(d, arr):
    count = 0
    for i, a in enumerate(arr):
        # check if the next two elements of the array have values that are d and 2d greater than the current element
        if a + d in arr[i + 1 :] and a + 2 * d in arr[i + 1 :]:
            count += 1
    return count
