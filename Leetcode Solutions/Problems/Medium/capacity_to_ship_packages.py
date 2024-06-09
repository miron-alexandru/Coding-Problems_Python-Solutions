# problem link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days

# my solution:
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Define the search space
        left = max(weights)
        right = sum(weights)

        # Binary search
        while left < right:
            mid = (left + right) // 2
            required_days = 1
            current_load = 0

            # Simulate the loading process
            for weight in weights:
                if current_load + weight > mid:
                    required_days += 1
                    current_load = 0

                current_load += weight

            if required_days <= days:
                right = mid
            else:
                left = mid + 1

        return left