# Problem Link: https://www.codewars.com/kata/53d3173cf4eb7605c10001a8/


# My Solution:
def power(lst):
    if not lst:
        return [[]]
    else:
        rest = power(lst[1:])
        return rest + [[lst[0]] + x for x in rest]
