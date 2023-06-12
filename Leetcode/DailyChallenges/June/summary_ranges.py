# problem link: https://leetcode.com/problems/summary-ranges


# my solution:
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        i = 0

        while i < len(nums):
            start = end = nums[i]

            # Find the end of the consecutive sequence
            while i + 1 < len(nums) and nums[i + 1] == end + 1:
                end = nums[i + 1]
                i += 1

            # Create the range string
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(str(start) + "->" + str(end))

            i += 1

        return ranges