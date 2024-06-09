# Given the participants' score sheet for your University Sports Day
# you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score
# of the runner-up

# Input format
# The first line contains n. The second lien contains an array A[] of
# n integers each separated by a space.


# Output format
# Print te runner-up score

# Sample input
# 5
# 2 3 6 6 5

# Sample output
# 5


# My Solution
n = int(input())
arr = map(int, input().split())
print(sorted(set(arr), reverse=True)[1])
