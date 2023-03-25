# Problem Link: https://www.hackerrank.com/challenges/anagram/problem


# My Solution:
def anagram(s):
    if len(s) % 2 != 0:
        return -1
    else:
        # calculate the length of each substring and split the string into two substrings
        half_len = len(s) // 2
        s1 = s[:half_len]
        s2 = s[half_len:]
        # initialize the frequency arrays for both
        freq_s1 = [0] * 26
        freq_s2 = [0] * 26
        # count the frequency of each letter in both substrings
        for i in range(half_len):
            freq_s1[ord(s1[i]) - ord('a')] += 1

        for i in range(half_len):
            freq_s2[ord(s2[i]) - ord('a')] += 1
        # calculate absolute difference between the frequencies of each letter
        counter = 0
        for i in range(26):
            counter += abs(freq_s1[i] - freq_s2[i])

        return counter // 2
