from collections import defaultdict


def power_of_two(x):
    return x and (not (x & (x - 1)))


def countPairs(arr):
    dic = defaultdict(int)
    for x in arr:
        dic[x] += 1
    dic = list(dic.items())

    result = 0
    for i in range(len(dic)):
        a, a_count = dic[i]
        for j in range(i, len(dic)):
            b, b_count = dic[j]
            if power_of_two(a & b):
                if a == b:
                    result += (a_count * (a_count - 1)) // 2
                else:
                    result += a_count * b_count

    return result
