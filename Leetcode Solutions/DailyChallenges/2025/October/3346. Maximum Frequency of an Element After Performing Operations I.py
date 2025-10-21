# problem link: https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/


# Description:
"""
You are given an integer array nums and two integers k and numOperations.

You must perform an operation numOperations times on nums, where in each operation you:

Select an index i that was not selected in any previous operations.
Add an integer in the range [-k, k] to nums[i].
Return the maximum possible frequency of any element in nums after performing the operations.

 

Example 1:

Input: nums = [1,4,5], k = 1, numOperations = 2

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1]. nums becomes [1, 4, 5].
Adding -1 to nums[2]. nums becomes [1, 4, 4].
Example 2:

Input: nums = [5,11,20,20], k = 5, numOperations = 1

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1].
"""

# Solution:
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        frequency_count = defaultdict(int)
        range_contributions = defaultdict(int)
      
        for num in nums:
            frequency_count[num] += 1
            range_contributions[num] += 0
            range_contributions[num - k] += 1
            range_contributions[num + k + 1] -= 1
      
        max_frequency = 0
        current_sum = 0

        for position, contribution_delta in sorted(range_contributions.items()):
            current_sum += contribution_delta
            max_frequency = max(
                max_frequency, 
                min(current_sum, frequency_count[position] + numOperations)
            )
      
        return max_frequency