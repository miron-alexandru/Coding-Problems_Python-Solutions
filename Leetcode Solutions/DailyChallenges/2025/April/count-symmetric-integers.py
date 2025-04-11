# problem link: https://leetcode.com/problems/count-symmetric-integers/


# my solution:
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for num in range(low, high + 1):
            s = str(num)
            length = len(s)
            if length % 2 == 0:
                mid = length // 2
                first_half = sum(int(d) for d in s[:mid])
                second_half = sum(int(d) for d in s[mid:])
                if first_half == second_half:
                    count += 1

        return count
