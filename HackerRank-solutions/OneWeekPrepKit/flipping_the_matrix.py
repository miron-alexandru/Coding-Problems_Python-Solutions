# Problem Link: https://www.hackerrank.com/challenges/flipping-the-matrix/problem


# My Solution:
def flippingMatrix(matrix):
    # compute the size of the submatrix
    n = len(matrix) // 2

    max_sum = 0
    # loop over all positions in the upper left quadrant
    for i in range(n):
        for j in range(n):
            max_sum += max(matrix[i][j], matrix[i][2*n-1-j], matrix[2*n-1-i][j], matrix[2*n-1-i][2*n-1-j])

    return max_sum