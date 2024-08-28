# problem link: https://leetcode.com/problems/ugly-number-ii/



# my solution: 
import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Min-heap to store the ugly numbers
        heap = [1]
        # Set to keep track of the numbers that have been added to the heap
        seen = {1}
        
        # Prime factors
        primes = [2, 3, 5]
        
        # The variable to store the current ugly number
        ugly = 1
        
        for _ in range(n):
            # Pop the smallest ugly number
            ugly = heapq.heappop(heap)
            
            # Generate new ugly numbers by multiplying the current one by 2, 3, and 5
            for prime in primes:
                new_ugly = ugly * prime
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        
        # After n iterations, 'ugly' contains the nth ugly number
        return ugly
