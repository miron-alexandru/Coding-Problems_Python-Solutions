# Problem Link: https://www.hackerrank.com/challenges/smart-number/problem

# My Solution:
import math

def is_smart_number(num):
    val = int(math.sqrt(num))
    if val ** 2 == num:
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")