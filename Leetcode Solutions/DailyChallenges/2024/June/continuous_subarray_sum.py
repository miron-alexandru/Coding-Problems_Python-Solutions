# problem link: https://leetcode.com/problems/continuous-subarray-sum/


# my solution:
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Edge case
        if len(nums) < 2:
            return False

        # Initialize the remainder map with {0: -1} to handle subarrays starting from index 0
        remainder_map = {0: -1}
        current_sum = 0

        # Iterate through the array
        for i in range(len(nums)):
            current_sum += nums[i]
            remainder = current_sum % k

            # Normalize negative remainders to be positive
            if remainder < 0:
                remainder += k

            # Check if this remainder has been seen before
            if remainder in remainder_map:
                # Check the distance between current index and stored index
                if i - remainder_map[remainder] > 1:
                    return True
            else:
                # Store the index of this remainder
                remainder_map[remainder] = i

        return False
