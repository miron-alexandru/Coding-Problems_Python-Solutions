# problem link: https://leetcode.com/problems/number-of-zigzag-arrays-i/


# Description:
"""
You are given three integers n, l, and r.

A ZigZag array of length n is defined as follows:

Each element lies in the range [l, r].
No two adjacent elements are equal.
No three consecutive elements form a strictly increasing or strictly decreasing sequence.
Return the total number of valid ZigZag arrays.

Since the answer may be large, return it modulo 109 + 7.

A sequence is said to be strictly increasing if each element is strictly greater than its previous one (if exists).

A sequence is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).

 

Example 1:

Input: n = 3, l = 4, r = 5

Output: 2

Explanation:

There are only 2 valid ZigZag arrays of length n = 3 using values in the range [4, 5]:

[4, 5, 4]
[5, 4, 5]​​​​​​​
Example 2:

Input: n = 3, l = 1, r = 3

Output: 10

Explanation:

There are 10 valid ZigZag arrays of length n = 3 using values in the range [1, 3]:

[1, 2, 1], [1, 3, 1], [1, 3, 2]
[2, 1, 2], [2, 1, 3], [2, 3, 1], [2, 3, 2]
[3, 1, 2], [3, 1, 3], [3, 2, 3]
All arrays meet the ZigZag conditions.
"""

# Solution:

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m

        # Initialize for position 1 (0-indexed), having placed first element
        # No direction yet; for position 2 we choose freely (any v != first)
        # Bootstrap: treat first step separately.
        # up[v] = ways ending at v with last step up
        # dn[v] = ways ending at v with last step down

        up = [0] * m
        dn = [0] * m

        # Place first two elements: for each pair (a, b) with a != b
        # if b > a: up[b] += 1 for each valid a < b → up[b] = b
        # if b < a: dn[b] += 1 for each valid a > b → dn[b] = m-1-b
        for v in range(m):
            up[v] = v          # number of values below v
            dn[v] = m - 1 - v  # number of values above v

        for _ in range(n - 2):
            # prefix sum of dn for new_up
            prefix_dn = [0] * (m + 1)
            for v in range(m):
                prefix_dn[v + 1] = (prefix_dn[v] + dn[v]) % MOD

            # suffix sum of up for new_dn
            suffix_up = [0] * (m + 1)
            for v in range(m - 1, -1, -1):
                suffix_up[v] = (suffix_up[v + 1] + up[v]) % MOD

            new_up = [0] * m
            new_dn = [0] * m
            for w in range(m):
                new_up[w] = prefix_dn[w]          # sum dn[0..w-1]
                new_dn[w] = suffix_up[w + 1]      # sum up[w+1..m-1]

            up, dn = new_up, new_dn

        return (sum(up) + sum(dn)) % MOD