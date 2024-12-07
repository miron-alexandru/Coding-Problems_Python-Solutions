# problem link: https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/


# my solution:
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canDistribute(max_balls: int) -> bool:
            operations = 0
            for balls in nums:
                # Calculate number of operations needed for this bag
                operations += (balls - 1) // max_balls
                if operations > maxOperations:
                    return False
            return True
        
        # Binary search bounds
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid  # Try for a smaller penalty
            else:
                left = mid + 1  # Increase penalty
        return left