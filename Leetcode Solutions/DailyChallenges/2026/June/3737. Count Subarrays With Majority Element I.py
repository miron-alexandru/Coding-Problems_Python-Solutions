# Problem link: https://leetcode.com/problems/count-subarrays-with-majority-element-i/

# Description:
"""
You are given an integer array nums and an integer target.

Return the number of subarrays of nums in which target is the majority element.

The majority element of a subarray is the element that appears strictly more than half of the times in that subarray.

 

Example 1:

Input: nums = [1,2,2,3], target = 2

Output: 5

Explanation:

Valid subarrays with target = 2 as the majority element:

nums[1..1] = [2]
nums[2..2] = [2]
nums[1..2] = [2,2]
nums[0..2] = [1,2,2]
nums[1..3] = [2,2,3]
So there are 5 such subarrays.

Example 2:

Input: nums = [1,1,1,1], target = 1

Output: 10

Explanation:

All 10 subarrays have 1 as the majority element.

Example 3:

Input: nums = [1,2,3], target = 4

Output: 0

Explanation:

target = 4 does not appear in nums at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0.
"""

# Solution:
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1  # prefix sum of 0 before any elements
        
        prefix = 0
        less_count = 0  # number of past prefix sums strictly < current prefix
        result = 0
        
        for num in nums:
            if num == target:
                prefix += 1
                # prefix just increased: freq[prefix-1] entries are now < prefix
                less_count += freq[prefix - 1]
            else:
                prefix -= 1
                # prefix just decreased: freq[prefix] entries are no longer < prefix
                less_count -= freq[prefix]
            
            result += less_count
            freq[prefix] += 1
        
        return result
