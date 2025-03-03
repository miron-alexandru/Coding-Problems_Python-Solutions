# problem link: https://leetcode.com/problems/partition-array-according-to-given-pivot/


# my solution:
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than, greater_than, equal_to = [], [], []

        for n in nums:
            if n < pivot:
                less_than.append(n)
            elif n == pivot:
                equal_to.append(n)
            else:
                greater_than.append(n)

        result = less_than + equal_to + greater_than 

        return result

