# problem link: https://www.hackerrank.com/challenges/countingsort1/problem


# my solution:
def countingSort(arr):
    freq = [0] * 100
    for n in arr:
        freq[n] += 1  # increment the counter at the index corresponding to the value
    return freq
