# problem link: https://leetcode.com/problems/maximum-score-from-removing-substrings/


# Description:
"""
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
."""

# Solution:
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Determine the more valuable pair to remove first: ab or ba
        first_char, second_char = "a", "b"
        if x < y:
            x, y = y, x
            first_char, second_char = second_char, first_char

        total_gain = 0
        first_count = 0
        second_count = 0

        for char in s:
            if char == first_char:
                first_count += 1
            elif char == second_char:
                if first_count:
                    # Remove a high-value pair either ab or ba
                    total_gain += x
                    first_count -= 1
                else:
                    second_count += 1
            else:
                # On encountering a non matching character process remaining lower priority pairs
                total_gain += min(first_count, second_count) * y
                first_count = second_count = 0

        # Final processing for any remaining unmatched characters
        total_gain += min(first_count, second_count) * y
        return total_gain
