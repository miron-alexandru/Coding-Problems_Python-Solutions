# problem link: https://www.hackerrank.com/challenges/np-polynomials/problem


# solution:
import numpy as np

coefficients = list(map(float, input().split()))
x = float(input())

# evaluate polynomial at x
result = np.polyval(coefficients, x)

print(result)
