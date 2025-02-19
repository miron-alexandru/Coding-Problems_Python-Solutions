# problem link: https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/



# my solution:
import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)  # Convert nums into a min-heap
        operations = 0

        while nums[0] < k:
            if len(nums) < 2:
                break

            x = heapq.heappop(nums)  # Extract smallest
            y = heapq.heappop(nums)  # Extract second smallest
            new_value = (min(x, y) * 2 + max(x, y))
            heapq.heappush(nums, new_value)  # Push the new value back

            operations += 1  # Increment operation count

        return operations