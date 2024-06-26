# problem link: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/


# my solution:
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Deques to store the indices of elements in decreasing and increasing order
        max_deque = deque()
        min_deque = deque()
        
        # Initialize the left pointer of the sliding window and the longest subarray length
        left = 0
        longest = 0
        
        # Iterate over the array with the right pointer
        for right in range(len(nums)):
            # Maintain the max_deque to have elements in decreasing order
            while max_deque and nums[right] > nums[max_deque[-1]]:
                max_deque.pop()
            max_deque.append(right)
            
            # Maintain the min_deque to have elements in increasing order
            while min_deque and nums[right] < nums[min_deque[-1]]:
                min_deque.pop()
            min_deque.append(right)
            
            # Check if the current window satisfies the condition
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                # If not, shrink the window from the left
                if max_deque[0] == left:
                    max_deque.popleft()
                if min_deque[0] == left:
                    min_deque.popleft()
                left += 1
            
            # Update the longest subarray length
            longest = max(longest, right - left + 1)

        return longest
