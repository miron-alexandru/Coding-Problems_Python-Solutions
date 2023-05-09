# problem link: https://leetcode.com/problems/product-of-array-except-self


# my solution:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n

        # calculate products of all elements to the left and right of each element
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        # calculate product of all elements except self.
        answer = [left[i] * right[i] for i in range(n)]

        return answer