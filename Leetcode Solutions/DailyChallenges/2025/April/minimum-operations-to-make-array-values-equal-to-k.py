# problem link: https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/



# my solution:
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        unique_values = set()      # To track unique values in the array
        minimum_value = inf        # To keep track of the smallest value in nums

        for num in nums:
            # If any number is less than k it's impossible to reach k by only reducing values
            if num < k:
                return -1
            # Update minimum value seen so far
            minimum_value = min(minimum_value, num)
            # Add the number to the set of unique values
            unique_values.add(num)

        # The number of operations is the number of unique values that need to be reduced to k
        # If the smallest value in nums is already equal to k, we subtract 1 to avoid an unnecessary operation
        return len(unique_values) - int(minimum_value == k)