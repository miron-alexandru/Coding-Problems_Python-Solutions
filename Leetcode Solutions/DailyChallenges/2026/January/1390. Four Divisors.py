# problem link: https://leetcode.com/problems/four-divisors/



# Description:
"""
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

 

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation: 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
Example 2:

Input: nums = [21,21]
Output: 64
Example 3:

Input: nums = [1,2,3,4,5]
Output: 0
"""

# SOlution:
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0  # final answer

        for n in nums:
            if n < 6:
                continue  # too small to have four divisors

            limit = int(sqrt(n))  # only search up to square root
            count = 0            # number of divisors found
            div_sum = 0          # sum of divisors

            for i in range(1, limit + 1):
                if n % i != 0:
                    continue  # not a divisor

                pair = n // i  # matching divisor

                if i == pair:
                    count += 1
                    div_sum += i  # square root divisor
                else:
                    count += 2
                    div_sum += i + pair  # divisor pair

                if count > 4:
                    break  # no longer valid

            if count == 4:
                total += div_sum  # valid number

        return total
