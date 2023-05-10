# problem link: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem


# my solution:
def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i < len(c) - 1:
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
    return jumps
