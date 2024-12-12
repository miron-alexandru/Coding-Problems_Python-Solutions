# problem link: https://leetcode.com/problems/take-gifts-from-the-richest-pile/


# my solution:
import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Convert the number of gifts in each pile to negative values to simulate a max-heap
        # Using negative values allows to treat it as a max-heap
        max_heap = [-gift for gift in gifts]
        
        # Build the max-heap from the negative values
        heapq.heapify(max_heap)

        # Perform the operation for k seconds
        for _ in range(k):
            # Extract the largest pile by popping the smallest (most negative) value
            largest_pile = -heapq.heappop(max_heap)
            
            # Calculate the remaining gifts after taking the square root
            remaining_gifts = int(largest_pile ** 0.5)
            
            # Push the remaining gifts back into the heap as a negative value
            heapq.heappush(max_heap, -remaining_gifts)

        # Calculate the sum of the remaining gifts in all piles
        return -sum(max_heap)
