# problem link: https://leetcode.com/problems/fibonacci-number


# my solution:
class Solution:
    def fib(self, n: int) -> int:
        # Base case
        if n <= 1:
            return n

        # Initialize two variables a and b to 0 and 1
        a, b = 0, 1

        # Loop n-1 times to calculate F(n)
        for i in range(2, n + 1):
            # Calculate the sum of a and b
            c = a + b
            # Update a to be b
            a = b
            # Update b to be c
            b = c

        # Return the value of b, which is F(n)
        return b
