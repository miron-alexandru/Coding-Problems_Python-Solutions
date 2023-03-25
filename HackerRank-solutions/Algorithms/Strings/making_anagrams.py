# Problem Link: https://www.hackerrank.com/challenges/making-anagrams/problem


# My Solution:

def makingAnagrams(s1, s2):
    freq_s1 = [0] * 26
    freq_s2 = [0] * 26
    # Count the frequency of each letter in the both strings
    for c in s1:
        freq_s1[ord(c) - ord('a')] += 1

    for c in s2:
        freq_s2[ord(c) - ord('a')] += 1
    # calculate the absolute difference between freqs of each letter
    counter = 0
    for i in range(26):
        counter += abs(freq_s1[i] - freq_s2[i])
