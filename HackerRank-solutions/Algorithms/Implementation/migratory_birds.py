# problem link: https://www.hackerrank.com/challenges/migratory-birds/problem


# my solution:
def migratoryBirds(arr):
    freq = {}
    for bird in arr:
        freq[bird] = freq.get(bird, 0) + 1

    max_freq = max(freq.values())
    most_freq_birds = [k for k, v in freq.items() if v == max_freq]

    return min(most_freq_birds)
