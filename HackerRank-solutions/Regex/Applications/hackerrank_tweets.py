# problem link: https://www.hackerrank.com/challenges/hackerrank-tweets/problem

# my solution:
# without regex
n = int(input())
count = 0
for t in range(n):
    tweet = input().lower()
    if "hackerrank" in tweet:
        count += 1
print(count)

# usign regex:
import re

n = int(input())
count = 0
pattern = re.compile(r'hackerrank', re.IGNORECASE)

for i in range(n):
    tweet = input()
    if re.search(pattern, tweet):
        count += 1

print(count)
