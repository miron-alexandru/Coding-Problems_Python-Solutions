# problem link: https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/


# solution:
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Helper function to calculate sum of digits of a number
        def digit_sum(n: int) -> int:
            return sum(int(digit) for digit in str(n))
        
        # Dictionary to group numbers by their sum of digits
        digit_groups = {}
        
        # Group numbers by the sum of their digits
        for num in nums:
            d_sum = digit_sum(num)
            if d_sum not in digit_groups:
                digit_groups[d_sum] = []
            digit_groups[d_sum].append(num)
        
        max_sum = -1
        
        # Iterate over the digit groups and find the maximum sum of two numbers
        for group in digit_groups.values():
            if len(group) > 1:
                # Sort the group to easily get the two largest numbers
                group.sort(reverse=True)
                max_sum = max(max_sum, group[0] + group[1])
        
        return max_sum
