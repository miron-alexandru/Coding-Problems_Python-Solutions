# Problem Link: https://www.hackerrank.com/challenges/palindrome-index/problem


# My Solution:
def palindromeIndex(s):
    n = len(s)
    # check only the first half of the string
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            # check if removing the character at position i or position n-i-1 makes the rest of the string a palindrome
            if s[i + 1 : n - i] == s[i + 1 : n - i][::-1]:
                return i
            elif s[i : n - i - 1] == s[i : n - i - 1][::-1]:
                return n - i - 1
            else:
                return -1
    return -1
