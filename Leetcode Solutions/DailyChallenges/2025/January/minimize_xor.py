# probleem link: https://leetcode.com/problems/minimize-xor/



# solution:
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count = num2.bit_count()
        x = 0
        for i in range(30, -1, -1):
            if num1 >> i & 1 and count:
                x |= 1 << i
                count -= 1
        for i in range(30):
            if num1 >> i & 1 ^ 1 and count:
                x |= 1 << i
                count -= 1
        return x