# problem link: https://leetcode.com/problems/bitwise-xor-of-all-pairings/


# my solution:
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor_nums1 = 0
        xor_nums2 = 0
        
        # Compute XOR of nums1
        for num in nums1:
            xor_nums1 ^= num
        
        # Compute XOR of nums2
        for num in nums2:
            xor_nums2 ^= num
        
        # Determine the final XOR result
        result = 0
        if len(nums2) % 2 == 1:
            result ^= xor_nums1
        if len(nums1) % 2 == 1:
            result ^= xor_nums2
        
        return result