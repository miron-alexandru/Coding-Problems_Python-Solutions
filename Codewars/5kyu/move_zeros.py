# Problem link: https://www.codewars.com/kata/52597aa56021e91c93000cb0


# My Solution:
def move_zeros(lst):
    zero_count = lst.count(0)
    lst = [x for x in lst if x != 0]
    return lst + [0] * zero_count
