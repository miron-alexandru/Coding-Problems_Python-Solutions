# Problem Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-caesar-cipher-1/problem


# My Solution:
def caesarCipher(s, k):
    result = ""
    for c in s:
        if c.isalpha():
            if c.isupper():
                base = ord("A")
            else:
                base = ord("a")
            result += chr((ord(c) - base + k) % 26 + base)
        else:
            result += c
    return result
