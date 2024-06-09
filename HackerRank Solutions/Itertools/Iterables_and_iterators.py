# Problem Link: https://www.hackerrank.com/challenges/iterables-and-iterators/problem


# My Solution:
import itertools as it

n = int(input())
letters = input().split()
k = int(input())

# count indices containing 'a'
count_a = letters.count("a")

count_no_a = 0
for indices in it.combinations(letters, k):
    if "a" not in indices:
        count_no_a += 1

# compute the probability
prob = 1 - count_no_a / len(list(it.combinations(letters, k)))

print(prob)
