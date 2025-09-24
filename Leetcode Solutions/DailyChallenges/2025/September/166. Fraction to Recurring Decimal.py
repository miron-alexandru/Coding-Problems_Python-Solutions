# problem link: https://leetcode.com/problems/fraction-to-recurring-decimal/


# Description:
"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"
"""


# Solution:
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        # handle sign
        sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
        n, d = abs(numerator), abs(denominator)

        # integer part
        integer = n // d
        remainder = n % d
        result = sign + str(integer)

        # no fraction if no remainder
        if remainder == 0:
            return result

        result += "."
        seen = {}      # map remainder -> index in digits
        digits = []    # fractional digits

        # simulate long division
        while remainder and remainder not in seen:
            seen[remainder] = len(digits)
            remainder *= 10
            digits.append(str(remainder // d))
            remainder %= d

        # if remainder ends, no repeat
        if remainder == 0:
            result += "".join(digits)
        else:
            # repeat detected
            start = seen[remainder]
            non_repeat = "".join(digits[:start])
            repeat = "".join(digits[start:])
            result += non_repeat + "(" + repeat + ")"

        return result
