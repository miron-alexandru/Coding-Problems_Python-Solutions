# Problem Link: https://www.codewars.com/kata/54da5a58ea159efa38000836


# My Solution:
arr = [5, 5, 5]

def find_it(seq):
	return next(n for n in seq if seq.count(n) % 2 == 1)

