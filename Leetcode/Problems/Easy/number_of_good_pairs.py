# problem link: https://leetcode.com/problems/number-of-good-pairs


# my solutions:
# 1
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count

# 2
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        num_counts = [0] * 101
        
        for num in nums:
            count += num_counts[num]
            num_counts[num] += 1
        
        return count


