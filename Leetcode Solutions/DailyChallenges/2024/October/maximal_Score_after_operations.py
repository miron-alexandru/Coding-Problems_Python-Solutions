# problem link: https://leetcode.com/problems/maximal-score-after-applying-k-operations/


# my solution:
import heapq
from math import ceil

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Create a max-heap (store negative values for max-heap simulation)
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        score = 0
        
        # Perform k operations
        for _ in range(k):
            # Extract the largest element (smallest negative)
            largest = -heapq.heappop(max_heap)
            
            # Add the largest element to the score
            score += largest
            
            # Compute the new value (ceil(largest / 3))
            new_val = ceil(largest / 3)
            
            heapq.heappush(max_heap, -new_val)
        
        return score
