# problem link:https://leetcode.com/problems/neighboring-bitwise-xor/



# my solution:

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # XOR all elements in the derived array
        xor_sum = 0
        for num in derived:
            xor_sum ^= num
        # If the XOR of all elements is 0, a valid original array exists
        return xor_sum == 0
