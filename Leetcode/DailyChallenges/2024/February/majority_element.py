# problem link: https://leetcode.com/problems/majority-element/



# my solution:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_element = None
        count = 0
        
        for num in nums:
            if count == 0:
                max_element = num
                count = 1
            elif num == max_element:
                count += 1
            else:
                count -= 1
                
        return max_element