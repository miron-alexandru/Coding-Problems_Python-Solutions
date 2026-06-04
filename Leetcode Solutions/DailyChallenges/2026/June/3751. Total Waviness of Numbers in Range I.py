# problem link: https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/


# Description:
"""
You are given two integers num1 and num2 representing an inclusive range [num1, num2].

The waviness of a number is defined as the total count of its peaks and valleys:

A digit is a peak if it is strictly greater than both of its immediate neighbors.
A digit is a valley if it is strictly less than both of its immediate neighbors.
The first and last digits of a number cannot be peaks or valleys.
Any number with fewer than 3 digits has a waviness of 0.
Return the total sum of waviness for all numbers in the range [num1, num2].
 

Example 1:

Input: num1 = 120, num2 = 130

Output: 3

Explanation:

In the range [120, 130]:
120: middle digit 2 is a peak, waviness = 1.
121: middle digit 2 is a peak, waviness = 1.
130: middle digit 3 is a peak, waviness = 1.
All other numbers in the range have a waviness of 0.
Thus, total waviness is 1 + 1 + 1 = 3.

Example 2:

Input: num1 = 198, num2 = 202

Output: 3

Explanation:

In the range [198, 202]:
198: middle digit 9 is a peak, waviness = 1.
201: middle digit 0 is a valley, waviness = 1.
202: middle digit 0 is a valley, waviness = 1.
All other numbers in the range have a waviness of 0.
Thus, total waviness is 1 + 1 + 1 = 3.

Example 3:

Input: num1 = 4848, num2 = 4848

Output: 2

Explanation:

Number 4848: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.
"""

#Solution:
from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(n: int) -> int:
            if n < 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            @lru_cache(None)
            def dp(pos, tight, started, length, prev1, prev2):
                if pos == m:
                    return (1, 0)  # (count of numbers, total waviness)

                limit = digits[pos] if tight else 9

                total_count = 0
                total_waviness = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            False,
                            0,
                            10,
                            10,
                        )
                        total_count += cnt
                        total_waviness += wav
                        continue

                    if not started:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            1,
                            d,
                            10,
                        )
                        total_count += cnt
                        total_waviness += wav
                        continue

                    extra = 0
                    if length >= 2:
                        if (prev1 > prev2 and prev1 > d) or (
                            prev1 < prev2 and prev1 < d
                        ):
                            extra = 1

                    nlength = min(2, length + 1)

                    cnt, wav = dp(
                        pos + 1,
                        ntight,
                        True,
                        nlength,
                        d,
                        prev1,
                    )

                    total_count += cnt
                    total_waviness += wav + extra * cnt

                return (total_count, total_waviness)

            return dp(0, True, False, 0, 10, 10)[1]

        return solve(num2) - solve(num1 - 1)