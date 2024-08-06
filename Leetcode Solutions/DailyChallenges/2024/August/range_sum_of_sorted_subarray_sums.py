# problem link: https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/


# my solution:
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        
        # List to store all subarray sums
        subarray_sums = []
        
        # Compute all subarray sums
        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += nums[end]
                subarray_sums.append(current_sum)
        
        # Sort the subarray sums
        subarray_sums.sort()
        
        # Compute the sum from index left to right
        result = sum(subarray_sums[left-1:right]) % MOD
        
        return result