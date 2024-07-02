# problem link: https://leetcode.com/problems/intersection-of-two-arrays-ii/


# my solution:
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # count freq for both arrays
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        # find common elements and their freq
        common = []
        for num in count1.keys():
            if num in count2:
                common += [num] * min(count1[num], count2[num])

        return common