# Given an integer, n, perform the following conditional actions:
# If n is odd, prind Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater then 20, print Not Weird

# Input Format
# A single line containing a positive integer, n

# Constraints
# 1 < n <= 100

# Output format
# Print Weird if the number is weird. Otherwise print Not Weird

# Sample Input
# 3

# Sample Output
# Weird

# My solution:
if __name__ == "__main__":
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif n in range(2, 6) and n % 2 == 0:
        print("Not Weird")
    elif n in range(6, 21) and n % 2 == 0:
        print("Weird")
    elif n > 20 and n % 2 == 0:
        print("Not Weird")
