# problem link: https://leetcode.com/problems/merge-strings-alternately


# my solution:
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum number of candies
        max_candies = max(candies)
        
        # Initialize result array
        n = len(candies)
        result = [False] * n
        
        # Iterate over candies and update result array
        for i in range(n):
            if candies[i] + extraCandies >= max_candies:
                result[i] = True

        return result
