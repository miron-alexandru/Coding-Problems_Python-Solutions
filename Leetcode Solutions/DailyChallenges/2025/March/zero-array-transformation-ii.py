# problem link: https://leetcode.com/problems/zero-array-transformation-ii/


# solution:
from bisect import bisect_left

class Solution:
    def minZeroArray(self, nums: List[int], operations: List[List[int]]) -> int:
        def is_valid(operation_count: int) -> bool:
            prefix_diff = [0] * (len(nums) + 1)
            
            for start, end, value in operations[:operation_count]:
                prefix_diff[start] += value
                prefix_diff[end + 1] -= value
            
            current_sum = 0
            for original_value, delta in zip(nums, prefix_diff):
                current_sum += delta
                if original_value > current_sum:
                    return False
            
            return True

        total_operations = len(operations)
        min_operations = bisect_left(range(total_operations + 1), True, key=is_valid)
        
        return -1 if min_operations > total_operations else min_operations
