# Problem Link: https://leetcode.com/problems/merge-sorted-array/


# My Solution:
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # initialize three pointers
        i, j, k = m - 1, n - 1, m + n - 1
        # compare elements at nums1[i] and nums2[j]
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
