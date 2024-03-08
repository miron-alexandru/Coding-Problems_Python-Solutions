# problem link: https://leetcode.com/problems/count-elements-with-maximum-frequency/


# my solution:
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        # Find max freq
        max_freq = max(freq_dict.values())

        # Count how many elements have the maximum frequency
        max_freq_elements = sum(1 for freq in freq_dict.values() if freq == max_freq)

        return max_freq * max_freq_elements