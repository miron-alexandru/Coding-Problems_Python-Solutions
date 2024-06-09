# Problem Link: https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9


# My Solution:
def find_short(s):
    shortest = min(s.split(), key=len)
    return len(shortest)
