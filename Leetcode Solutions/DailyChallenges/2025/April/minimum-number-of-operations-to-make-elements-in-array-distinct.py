# problem link: https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/


# my solution:

#1.
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0

        while len(nums) != len(set(nums)):
            nums = nums[3:]
            operations += 1

        return operations



#2.
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0

        while True:
            seen = set()
            found = False

            for num in nums:
                if num in seen:
                    found = True
                    break

                seen.add(num)

            if not found:
                break
            
            nums = nums[3:]
            operations += 1

        return operations




