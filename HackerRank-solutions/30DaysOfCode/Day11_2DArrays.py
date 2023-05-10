# Problem Link: https://www.hackerrank.com/challenges/30-2d-arrays/problem


# My Solution:
arr = []
for i in range(6):
    arr.append(list(map(int, input().rstrip().split())))

max_sum = -63  # The minimum possible sum is -9 * 7 = -63
for i in range(4):
    for j in range(4):
        sum = (
            arr[i][j]
            + arr[i][j + 1]
            + arr[i][j + 2]
            + arr[i + 1][j + 1]
            + arr[i + 2][j]
            + arr[i + 2][j + 1]
            + arr[i + 2][j + 2]
        )
        max_sum = max(max_sum, sum)

print(max_sum)
