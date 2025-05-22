# problem link: https://leetcode.com/problems/zero-array-transformation-iii/


# description:
"""
You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri].

Each queries[i] represents the following action on nums:

Decrement the value at each index in the range [li, ri] in nums by at most 1.
The amount by which the value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.

Return the maximum number of elements that can be removed from queries, such that nums can still be converted to a zero array using the remaining queries. If it is not possible to convert nums to a zero array, return -1.

 

Example 1:

Input: nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]

Output: 1

Explanation:

After removing queries[2], nums can still be converted to a zero array.

Using queries[0], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
Using queries[1], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
Example 2:

Input: nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]

Output: 2

Explanation:

We can remove queries[2] and queries[3].

Example 3:

Input: nums = [1,2,3,4], queries = [[0,3]]

Output: -1

Explanation:

nums cannot be converted to a zero array even after using all the queries.
"""

# Solution:
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # Sort the queries by their start indices
        queries.sort()
        
        max_heap = []  # A max-heap to store the end indices of valid queries
        diff_array = [0] * (len(nums) + 1)  # Difference array for range updates
        prefix_sum = 0  # Accumulated prefix sum
        query_index = 0  # Index to iterate over sorted queries

        for i, target in enumerate(nums):
            # Update prefix sum for current index using difference array
            prefix_sum += diff_array[i]

            # Add all queries that start at or before index i to the heap
            while query_index < len(queries) and queries[query_index][0] <= i:
                # Push the end index of the query to the heap (negated for max-heap)
                heappush(max_heap, -queries[query_index][1])
                query_index += 1

            # While prefix sum is less than current target and we have valid queries to use
            while prefix_sum < target and max_heap and -max_heap[0] >= i:
                # Use one removal operation
                prefix_sum += 1

                # Get the query with the latest valid end index
                end_index = -heappop(max_heap)

                # Mark the end of the effect of this operation in the difference array
                diff_array[end_index + 1] -= 1

            # If even after using available queries we can't reach target return -1
            if prefix_sum < target:
                return -1

        return len(max_heap)