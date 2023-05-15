# problem link: https://www.hackerrank.com/challenges/alternating-characters/problem


# my solution:
def alternatingCharacters(s):
    deletions = 0
    for ind in range(1, len(s)):
        if s[ind] == s[ind - 1]:
            deletions += 1
    return deletions