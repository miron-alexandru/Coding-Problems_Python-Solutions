# problem link: https://www.hackerrank.com/challenges/permutation-equation/problem


# my solution:
def permutationEquation(p):
    n = len(p)
    ind = {p[i]: i + 1 for i in range(n)}
    result = []

    for x in range(1, n + 1):
        ind_x = ind[x]
        ind_ind_x = ind[ind_x]
        result.append(ind_ind_x)

    return result
