# problem link: https://leetcode.com/problems/partition-equal-subset-sum/


# my solution:
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If the total sum is odd we cannot divide it into two equal subsets
        if total_sum % 2 != 0:
            return False

        # The target sum for each subset is half of the total
        target = total_sum // 2

        # This set keeps track of all possible subset sums we've seen so far
        possible_sums = set()
        possible_sums.add(0)  # We can always make a sum of 0 with an empty subset

        for num in nums:
            new_nums = set()
            # For each existing possible sum add the current number to it
            for s in possible_sums:
                new_sum = s + num
                # If we reach the target sum we can partition the array
                if new_sum == target:
                    return True
                new_nums.add(new_sum)  # Track new possible sums
            # Update the set with new possible sums generated in this iteration
            possible_sums.update(new_nums)

        return target in possible_sums
