# Problem link: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem


# Solution:

from collections import defaultdict

n, m = map(int, input().split())
word_group_a = defaultdict(list)
for i in range(n):
    word = input().strip()
    word_group_a[word].append(i+1)

for i in range(m):
    word = input().strip()
    if word in word_group_a:
        print(*word_group_a[word])
    else:
        print(-1)
