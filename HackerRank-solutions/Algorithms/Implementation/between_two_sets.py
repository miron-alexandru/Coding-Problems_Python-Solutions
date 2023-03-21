# Problem Link: https://www.hackerrank.com/challenges/between-two-sets/problem


# My Solution:
def getTotalX(a, b):
    lcm = a[0]
    gcd = b[0]
   	count = 0

    for i in range(1, len(a)):
        lcm = (lcm * a[i]) // math.gcd(lcm, a[i])

    for i in range(1, len(b)):
        gcd = math.gcd(gcd, b[i])

    for i in range(lcm, gcd+1, lcm):
        if gcd % i == 0:
            count += 1
    
    return count
