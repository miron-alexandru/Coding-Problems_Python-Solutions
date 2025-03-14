# problem link: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/


# my solution:
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        low, high = 1, max(candies)
        res = 0
        
        def canDistribute(x):
            return sum(c // x for c in candies) >= k
        
        while low <= high:
            mid = (low + high) // 2
            if canDistribute(mid):
                res = mid  # Store valid answer
                low = mid + 1  # Try for more candies per child
            else:
                high = mid - 1  # Reduce the possible value of x
        
        return res
