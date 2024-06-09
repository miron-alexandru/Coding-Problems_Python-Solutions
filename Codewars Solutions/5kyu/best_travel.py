# problem link: https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa

# my solution:
from itertools import combinations


def choose_best_sum(t, k, ls):
    best_sum = None
    for towns in combinations(ls, k):
        towns_sum = sum(towns)
        if towns_sum <= t and (best_sum is None or towns_sum > best_sum):
            best_sum = towns_sum
    return best_sum
