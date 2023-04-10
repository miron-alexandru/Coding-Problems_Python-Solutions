# problem link: https://www.hackerrank.com/challenges/equality-in-a-array/problem


# my solution:
def equalizeArray(arr):
    freq = {}
    max_freq = 0
    for n in arr:
        if n not in freq:
            freq[n] = 0
        freq[n] += 1
        max_freq = max(max_freq, freq[n])
    return len(arr) - max_freq
