# problem link: https://leetcode.com/problems/fruits-into-baskets-iii/


# Description:
"""
You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

From left to right, place the fruits according to these rules:

Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
Each basket can hold only one type of fruit.
If a fruit type cannot be placed in any basket, it remains unplaced.
Return the number of fruit types that remain unplaced after all possible allocations are made.

 

Example 1:

Input: fruits = [4,2,5], baskets = [3,5,4]

Output: 1

Explanation:

fruits[0] = 4 is placed in baskets[1] = 5.
fruits[1] = 2 is placed in baskets[0] = 3.
fruits[2] = 5 cannot be placed in baskets[2] = 4.
Since one fruit type remains unplaced, we return 1.

Example 2:

Input: fruits = [3,6,1], baskets = [6,4,7]

Output: 0

Explanation:

fruits[0] = 3 is placed in baskets[0] = 6.
fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
fruits[2] = 1 is placed in baskets[1] = 4.
Since all fruits are successfully placed, we return 0.
."""


# Solution:

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        N = 1
        while N <= n:
            N <<= 1  # next power of two >= n
        
        segTree = [0] * (2 * N)  # segment tree array
        
        for i in range(n):
            segTree[N + i] = baskets[i]  # set leaf nodes with basket capacities
        
        for i in range(N - 1, 0, -1):
            segTree[i] = max(segTree[2 * i], segTree[2 * i + 1])  # build tree with max values
        
        count = 0  # count of unplaced fruits
        for fruit in fruits:
            index = 1  # start from root
            if segTree[index] < fruit:
                count += 1  # no basket can hold this fruit
                continue
            
            # find basket with enough capacity using tree traversal
            while index < N:
                if segTree[2 * index] >= fruit:
                    index = 2 * index  # go left
                else:
                    index = 2 * index + 1  # go right
            
            segTree[index] = -1  # mark basket as used
            # update ancestors with new max values
            while index > 1:
                index //= 2
                segTree[index] = max(segTree[2 * index], segTree[2 * index + 1])
        
        return count
