# problem link: https://leetcode.com/problems/remove-duplicates-from-sorted-array



# my solution:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique_nums = list(set(nums))
        unique_nums.sort()
        nums[:len(unique_nums)] = unique_nums
        
        return len(unique_nums)
