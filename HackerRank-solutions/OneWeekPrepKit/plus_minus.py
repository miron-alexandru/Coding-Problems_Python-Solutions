# Problem Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem

# My SOlution:
def plusMinus(arr):
    n = len(arr)
    positive = format(sum(1 for i in arr if i > 0) / n, ".6f")
    negative = format(sum(1 for i in arr if i < 0) / n, ".6f")
    zeros = format(sum(1 for i in arr if i == 0) / n, ".6f")
    print(positive, negative, zeros, sep='\n')


