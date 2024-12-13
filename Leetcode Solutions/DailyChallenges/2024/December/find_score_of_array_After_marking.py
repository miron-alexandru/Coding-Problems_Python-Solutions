# problem link: https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/


# my solution:
import heapq

class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        n = len(nums)
        marked = [False] * n
        min_heap = []
        
        # Push all elements along with their indices into the heap
        for i, num in enumerate(nums):
            heapq.heappush(min_heap, (num, i))

        while min_heap:
            # Get the smallest unmarked element
            value, index = heapq.heappop(min_heap)
            
            # If this element is already marked skip it
            if marked[index]:
                continue

            # Mark this element and its adjacent elements
            marked[index] = True
            score += value

            # Mark the adjacent elements if they exist
            if index - 1 >= 0 and not marked[index - 1]:
                marked[index - 1] = True
            if index + 1 < n and not marked[index + 1]:
                marked[index + 1] = True
        
        return score
