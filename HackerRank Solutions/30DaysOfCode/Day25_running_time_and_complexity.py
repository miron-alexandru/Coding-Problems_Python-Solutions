# Problem Link: https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem


# My Solution:
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** (0.5)) + 1):
        if n % i == 0:
            return False
    return True


t = int(input())

for n in range(t):
    n = int(input())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")
