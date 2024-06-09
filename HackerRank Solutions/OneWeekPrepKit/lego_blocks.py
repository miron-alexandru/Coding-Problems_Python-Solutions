# Problem Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-lego-blocks/problem


# Solution: (Not mine. I was unable to solve this)


def tetranacci(n):
    arr = [1, 2, 4, 8]
    if n <= 4:
        return arr[:n]
    else:
        for i in range(4, n):
            arr.append(sum(arr[i - 4 : i]) % (10**9 + 7))
    return arr


def legoBlocks(n, m):
    MOD = 10**9 + 7
    a, s = [(v**n) % MOD for v in tetranacci(m)], [1]

    for i in range(1, len(a)):
        sums = sum([x * y for x, y in zip(a[:i], s[::-1])])
        s.append((a[i] - sums) % MOD)
    return s[-1]
