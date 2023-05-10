# problem link: https://www.hackerrank.com/challenges/python-sort-sort/problem

# my solution:
# Read the input
n, m = map(int, input().split())
rows = []
for i in range(n):
    row = list(map(int, input().split()))
    rows.append(row)
k = int(input())


# Define a function to extract the kth attribute from a row
def get_kth_attr(row):
    return row[k]


# Sort the rows based on the kth attribute
rows.sort(key=get_kth_attr)

# Print the sorted rows
for row in rows:
    print(*row)
