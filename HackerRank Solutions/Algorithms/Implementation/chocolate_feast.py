# problem link: https://www.hackerrank.com/challenges/chocolate-feast/problem


# my solutionn:
def chocolateFeast(n, c, m):
    choco_bought = n // c
    wrappers = choco_bought

    while wrappers >= m:
        free_chocos = wrappers // m
        choco_bought += free_chocos
        wrappers = wrappers % m + free_chocos

    return choco_bought
