# problem link: https://www.hackerrank.com/challenges/word-order/problem

# my solution:
n = int(input())
words = []
for i in range(n):
    words.append(input().strip())

# count the occurrences of each word
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# output the number of distinct words and their occurrences
print(len(word_count))
for word in words:
    if word_count[word] != 0:
        print(word_count[word], end=" ")
        word_count[word] = 0
