# problem link: https://www.hackerrank.com/challenges/funny-string/problem


# my solution:
def funnyString(s):
    r = s[::-1]
    n = len(s)
    diffs = [abs(ord(s[i]) - ord(s[i + 1])) for i in range(n - 1)]
    r_diffs = [abs(ord(r[i]) - ord(r[i + 1])) for i in range(n - 1)]
    if diffs == r_diffs:
        return "Funny"
    else:
        return "Not Funny"
