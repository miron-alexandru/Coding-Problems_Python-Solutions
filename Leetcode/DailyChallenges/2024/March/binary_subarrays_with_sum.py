# problem link: https://leetcode.com/problems/binary-subarrays-with-sum/


# my solution:
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        total_sum = 0
        # store the count of sums encountered
        sum_count = {0: 1}
        for num in nums:
            total_sum += num
            # If the current total sum - goal is in the dictionary means there's a subarray with the sum equal to the goal
            count += sum_count.get(total_sum - goal, 0)
            # Increment the count of the current total sum encountered
            sum_count[total_sum] = sum_count.get(total_sum, 0) + 1
        return count