# problem link: https://leetcode.com/problems/count-largest-group/

# Description:

"""
You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
 

Constraints:

1 <= n <= 104
"""

# My solutions:
# 1
class Solution:
    def countLargestGroup(self, n: int) -> int:
        group_counts = defaultdict(int)
        count = 0

        for num in range(1, n + 1):
            sums = 0
            for i in str(num):
                sums = sums + int(i)
            group_counts[sums] += 1

        max_value = max(group_counts.values())

        for value in group_counts.values():
            if value == max_value:
                count += 1

        return count


# 2 (Improved)        
class Solution:
    def countLargestGroup(self, n: int) -> int:
        group_counts = defaultdict(int)

        # Group numbers by the sum of their digits
        for num in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(num))
            group_counts[digit_sum] += 1

        # Find the size of the largest group
        max_group_size = max(group_counts.values())

        # Count how many groups have the largest size
        return sum(1 for count in group_counts.values() if count == max_group_size)