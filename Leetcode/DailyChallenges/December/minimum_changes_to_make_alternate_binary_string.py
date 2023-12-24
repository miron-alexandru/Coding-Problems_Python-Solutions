# problem link: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/


# my solution:
class Solution:
    def minOperations(self, s: str) -> int:
        min_operations_with_zero = 0
        min_operations_with_one = 0

        for i in range(len(s)):
            expected_char_0 = '0' if i % 2 == 0 else '1'
            expected_char_1 = '1' if i % 2 == 0 else '0'

            if s[i] != expected_char_0:
                min_operations_with_zero += 1

            if s[i] != expected_char_1:
                min_operations_with_one += 1

        return min(min_operations_with_zero, min_operations_with_one)
