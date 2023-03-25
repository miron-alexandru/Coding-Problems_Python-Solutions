# Problem Link: https://www.hackerrank.com/challenges/merge-the-tools/problem


# My Solution:
def merge_the_tools(s, k):
    for i in range(0, len(s), k):
        substring = s[i:i+k]
        unique_substring = ''.join(sorted(set(substring), key=substring.index))
        print(unique_substring)
