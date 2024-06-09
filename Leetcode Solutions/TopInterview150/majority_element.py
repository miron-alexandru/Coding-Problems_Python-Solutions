# problem link: https://leetcode.com/problems/majority-element


# my solution:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = {}
        for n in nums:
            if n in frequency:
                frequency[n] += 1
            else:
                frequency[n] = 1

        # find the highest frequency
        max_frequency = 0
        for e, freq in frequency.items():
            if freq > max_frequency:
                max_frequency = freq
                max_element = e

        return max_element
