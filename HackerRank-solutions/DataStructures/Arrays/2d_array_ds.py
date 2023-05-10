# problem link: https://www.hackerrank.com/challenges/2d-array/problem


# solution (not mine):
def hourglassSum(arr):
    max_sum = float("-inf")  # initialize the maximum sum to negative infinity
    for i in range(4):
        for j in range(4):
            # calculate the sum of the current hourglass
            hourglass_sum = (
                sum(arr[i][j : j + 3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j : j + 3])
            )
            # update the maximum sum if the current sum is greater
            if hourglass_sum > max_sum:
                max_sum = hourglass_sum
    return max_sum
