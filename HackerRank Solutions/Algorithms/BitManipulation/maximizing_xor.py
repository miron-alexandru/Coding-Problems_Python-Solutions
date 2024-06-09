# problem link: https://www.hackerrank.com/challenges/maximizing-xor/problem


# my solutionn:
def maximizingXor(l, r):
    max_xor = 0
    for i in range(l, r+1):
        for j in range(l, r+1):
            xor_result = i ^ j
            if xor_result > max_xor:
                max_xor = xor_result
    return max_xor