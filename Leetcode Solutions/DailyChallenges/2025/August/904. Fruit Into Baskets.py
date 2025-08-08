# problem link: https://leetcode.com/problems/fruit-into-baskets/


# Description:
"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2]..
"""


# Solution:
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0  # start of the sliding window
        counts = {}  # keeps track of fruit counts in the window
        max_len = 0  # stores the best window size found

        for right in range(len(fruits)):
            fruit_type = fruits[right]
            counts[fruit_type] = counts.get(fruit_type, 0) + 1  # add current fruit

            # shrink window if more than 2 fruit types
            while len(counts) > 2:
                left_fruit = fruits[left]
                counts[left_fruit] -= 1
                if counts[left_fruit] == 0:
                    del counts[left_fruit]  # remove fruit type if none left
                left += 1  # move start forward

            # update max length for current valid window
            max_len = max(max_len, right - left + 1)

        return max_len
