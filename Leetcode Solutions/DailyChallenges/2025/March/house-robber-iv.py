# problem link: https://leetcode.com/problems/house-robber-iv/


# solution:
from bisect import bisect_left

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can_steal_with_capability(capability: int) -> bool:
            """Returns True if it's possible to steal from at least k houses with max value ≤ capability."""
            houses_stolen = 0
            last_stolen_index = -2  # Ensures the first house can be stolen
            
            for current_index, money in enumerate(nums):
                if money > capability or current_index == last_stolen_index + 1:
                    continue  # Skip if house value exceeds capability or adjacent to the last stolen house
                
                houses_stolen += 1
                last_stolen_index = current_index  # Mark the current house as stolen
                
            return houses_stolen >= k

        return bisect_left(range(max(nums) + 1), True, key=can_steal_with_capability)
