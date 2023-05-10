# problem link: https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem


# my solution:
def hackerrankInString(s):
    k = 0
    for ind, i in enumerate(s):
        if s[ind] == "hackerrank"[k]:
            k += 1
        if k == len("hackerrank"):
            return "YES"
    return "NO"
