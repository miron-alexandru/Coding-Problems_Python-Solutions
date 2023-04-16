# problem link: https://leetcode.com/problems/merge-sorted-array

# my solution:
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # init three pointers
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        # Loop through the arrays and merge the larger num into the end of nums1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # if any nums remained in nums2, copy them at the start of nums 1
        nums1[:p2 + 1] = nums2[:p2 + 1]