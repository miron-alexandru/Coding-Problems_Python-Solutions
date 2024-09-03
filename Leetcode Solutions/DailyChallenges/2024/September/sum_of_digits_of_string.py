# problem link: https://leetcode.com/problems/sum-of-digits-of-string-after-convert/


# my solution:
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def string_to_number(s: str) -> int:
            """Convert a string to a number by replacing each letter with its position in the alphabet."""
            return int(''.join(str(ord(char) - ord('a') + 1) for char in s))
        
        def sum_of_digits(num: int) -> int:
            """Calculate the sum of the digits of a number."""
            return sum(int(digit) for digit in str(num))

        num = string_to_number(s)
        
        # Apply the digit sum transformation k times
        for _ in range(k):
            num = sum_of_digits(num)
        
        return num