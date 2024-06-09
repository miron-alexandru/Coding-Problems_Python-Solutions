# problem link: https://leetcode.com/problems/contiguous-array/

# my solution:

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        count = 0
        sum_indices = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if count in sum_indices:
                max_length = max(max_length, i - sum_indices[count])
            else:
                sum_indices[count] = i

        return max_length
