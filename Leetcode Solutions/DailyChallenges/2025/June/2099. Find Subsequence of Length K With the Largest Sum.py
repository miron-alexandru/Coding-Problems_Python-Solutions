# problem link: https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum


# Description:
"""
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.
Example 2:

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.
Example 3:

Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].
."""

# SOlutions:
#1.
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Attach the original index to each number
        with_index = []
        for i in range(len(nums)):
            with_index.append((nums[i], i))
        
        # Sort the list by number in descending order
        with_index.sort(key=lambda x: x[0], reverse=True)
        
        #Take the first k elements
        largest_k = with_index[:k]
        
        # Sort those k elements by their original position
        largest_k.sort(key=lambda x: x[1])

        result = []
        for num, idx in largest_k:
            result.append(num)
        
        return result

#2. using comprehensions
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Pair each number with its original index to preserve order later
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        # Sort by value in descending order and pick the top k elements
        top_k = sorted(indexed_nums, key=lambda x: x[0], reverse=True)[:k]
        
        # Sort the selected top k elements by their original indices to maintain subsequence order
        top_k_sorted_by_index = sorted(top_k, key=lambda x: x[1])

        return [num for num, _ in top_k_sorted_by_index]