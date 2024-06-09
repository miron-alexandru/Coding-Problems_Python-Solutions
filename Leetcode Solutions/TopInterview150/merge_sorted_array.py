# problem link: https://leetcode.com/problems/merge-sorted-array


# my solution:
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2[:n]
        nums1.sort()