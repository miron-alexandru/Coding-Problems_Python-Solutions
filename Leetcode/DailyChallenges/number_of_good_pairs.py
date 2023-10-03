# problem link: https://leetcode.com/problems/number-of-good-pairs


# my solution:
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        num_counts = [0] * 101
        
        for num in nums:
            count += num_counts[num]
            num_counts[num] += 1
        
        return count
