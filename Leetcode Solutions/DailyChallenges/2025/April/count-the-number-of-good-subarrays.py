# problem link: https://leetcode.com/problems/count-the-number-of-good-subarrays/


# solution:
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        frequency = Counter()
        result = current_pairs = 0
        left = 0

        for num in nums:
            current_pairs += frequency[num]
            frequency[num] += 1

            while current_pairs - frequency[nums[left]] + 1 >= k:
                frequency[nums[left]] -= 1
                current_pairs -= frequency[nums[left]]
                left += 1

            if current_pairs >= k:
                result += left + 1

        return result