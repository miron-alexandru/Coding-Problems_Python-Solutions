# Problem Link: https://www.hackerrank.com/challenges/a-very-big-sum/problem


# My Solution:
def aVeryBigSum(ar):
    big_sum = 0
    for i in range(0, len(ar)):
        big_sum = big_sum + ar[i]
        
    return big_sum
