# problem link: https://leetcode.com/problems/sort-array-by-parity


# solutions:
# brute force:
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            if n % 2 == 0:
                result.insert(0, n)
            else:
                result.append(n)
        return result


# two pointers approach:
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
    
        while left < right:
            if nums[left] % 2 == 1 and nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
            
            if nums[left] % 2 == 0:
                left += 1
            
            if nums[right] % 2 == 1:
                right -= 1
        
        return nums
