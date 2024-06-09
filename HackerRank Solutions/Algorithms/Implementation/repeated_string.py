# problem link: https://www.hackerrank.com/challenges/repeated-string/problem


# my solution:
def repeatedString(s, n):
    count_a = s.count("a")
    full_repeats = n // len(s)
    full_a = count_a * full_repeats
    remainder = n % len(s)
    for i in range(remainder):
        if s[i] == "a":
            full_a += 1
    return full_a
