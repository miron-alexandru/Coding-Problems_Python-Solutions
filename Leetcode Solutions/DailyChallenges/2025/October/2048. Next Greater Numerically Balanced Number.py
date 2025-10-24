# problem link: https://leetcode.com/problems/next-greater-numerically-balanced-number/


# Description:
"""
An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.

Given an integer n, return the smallest numerically balanced number strictly greater than n.

 

Example 1:

Input: n = 1
Output: 22
Explanation: 
22 is numerically balanced since:
- The digit 2 occurs 2 times. 
It is also the smallest numerically balanced number strictly greater than 1.
Example 2:

Input: n = 1000
Output: 1333
Explanation: 
1333 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times. 
It is also the smallest numerically balanced number strictly greater than 1000.
Note that 1022 cannot be the answer because 0 appeared more than 0 times.
Example 3:

Input: n = 3000
Output: 3133
Explanation: 
3133 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 3000.
"""

# Solution:
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # Start checking from n + 1
        for candidate in count(n + 1):
            # Count the frequency of each digit in the current number
            digit_count = [0] * 10  # Array to store count of digits 0-9
            temp_num = candidate
          
            # Extract each digit and count its occurrences
            while temp_num > 0:
                temp_num, digit = divmod(temp_num, 10)
                digit_count[digit] += 1
          
            # Check if the number is beautiful:
            is_beautiful = all(
                count == 0 or digit == count 
                for digit, count in enumerate(digit_count)
            )
          
            if is_beautiful:
                return candidate