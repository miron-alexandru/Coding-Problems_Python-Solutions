# problem link: https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/


# Description:
"""
You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
Return the lexicographically smallest string that can be written on the paper.

 

Example 1:

Input: s = "zza"
Output: "azz"
Explanation: Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".
"""

# Solution:
class Solution:
    def robotWithString(self, s: str) -> str:
        remaining_chars = Counter(s)
        stack = []
        result = []

        for char in s:
            # Move the current character from s to the robots stack
            stack.append(char)

            # Decrement the count of this character from the remaining pool
            remaining_chars[char] -= 1
            if remaining_chars[char] == 0:
                del remaining_chars[char]

            # While the top of the stack can be safely written to result
            # and is not greater than any remaining character in s
            while stack and (not remaining_chars or stack[-1] <= min(remaining_chars)):
                result.append(stack.pop())

        return ''.join(result)

