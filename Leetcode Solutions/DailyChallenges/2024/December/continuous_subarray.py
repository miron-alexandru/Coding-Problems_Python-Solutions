# problem link: https://leetcode.com/problems/continuous-subarrays/


# solution:
from collections import deque

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = 0
        count = 0
        max_deque = deque()
        min_deque = deque()
        
        for right in range(len(nums)):
            # Maintain the decreasing order for the max_deque
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Maintain the increasing order for the min_deque
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # Shrink the window if the condition is violated
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                left += 1
                # Remove indices that are out of the window
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # Count valid subarrays ending at right
            count += (right - left + 1)
        
        return count
