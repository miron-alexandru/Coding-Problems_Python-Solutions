# List Comprehensions

# You are given three integers, x, y and z representing the dimensions
# of a cuboid along with an integer n. Print a list of all possible
# coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k
# is not equal to n. Here, 0 < i < x; 0 < i < y; 0 < k < z


# Example
# x = 1
# y = 1
# z = 2
# n = 3


# Input format
# Four integers xm ym z and n, each on a separate line.

# Constraints
# Print the list in lexicographic increasing order.

# Sample input
# 1
# 1
# 1
# 2

# Sample Output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


# My Solution: 

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ans = [[i, j, k] for i in range(x + 1) for j in range(y + 1)
    for k in range(z + 1) if i + j + k != n]
    print(ans)