# problem link: https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/


# my solution:
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        current_sum = 0
        count = 0
        
        for num in range(1, n + 1):
            if num in banned_set:  # Skip if the number is banned
                continue
            
            if current_sum + num > maxSum:  # Stop if adding this number exceeds maxSum
                break
            
            current_sum += num
            count += 1
        
        return count