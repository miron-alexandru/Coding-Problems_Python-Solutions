# problem link: https://www.hackerrank.com/challenges/cut-the-sticks/problem


# my solution:
def cutTheSticks(arr):
    arr.sort()
    count = len(arr)
    result = []
    while count > 0:
        result.append(count)
        shortest = arr[0]
        remaining = []
        for s in arr:
            if s > shortest:
                remaining.append(s - shortest)
        arr = remaining
        count = len(arr)
    return result