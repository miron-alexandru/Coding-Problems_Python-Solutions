# problem link: https://leetcode.com/problems/candy/description/


# Description:
"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
"""

# Solution:
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        
        # Initialize two arrays to keep track of candies from left to right and right to left passes
        # Every child gets at least one candy
        left = [1] * n
        right = [1] * n

        # Left to right
        # If a child has a higher rating than the one before they should get more candies
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        # Right to left
        # If a child has a higher rating than the one after they should get more candies
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        # For each child take the maximum number of candies required from both passes
        return sum(max(a, b) for a, b in zip(left, right))
