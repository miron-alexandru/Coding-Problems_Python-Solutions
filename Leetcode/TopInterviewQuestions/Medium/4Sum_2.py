# problem link: https://leetcode.com/problems/4sum-ii/


# my solution:
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        frequency = {}
        
        for num1 in nums1:
            for num2 in nums2:
                frequency[num1 + num2] = frequency.get(num1 + num2, 0) + 1
        
        count = 0
        
        for num3 in nums3:
            for num4 in nums4:
                count += frequency.get(-num3 - num4, 0)
        
        return count