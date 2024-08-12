# problem link: https://leetcode.com/problems/kth-largest-element-in-a-stream/


# my solution:
import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = []
        
        # Initialize the heap with the first k elements or fewer if there are not enough elements
        for num in nums:
            self.add(num)
    
    def add(self, val: int) -> int:
        # If the heap has fewer than k elements, push the new value
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        else:
            # If the heap has k elements, push the new value and pop the smallest
            if val > self.min_heap[0]:
                heapq.heappushpop(self.min_heap, val)
        
        # The root of the heap is the kth largest element
        return self.min_heap[0]
