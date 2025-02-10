# problem link: https://leetcode.com/problems/count-number-of-bad-pairs



# my solution:
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # Compute the total number of possible pairs
        n = len(nums)
        pairs = n * (n - 1) // 2
        # Dictionary to count occurrences of the key (j - nums[j])
        key_count = defaultdict(int)
        # good_pairs counter
        good_pairs = 0

        #Iterate through each index and compute key
        for j, num in enumerate(nums):
            key_j = j - num
            # Add the count of previous indices with the same key (good pairs)
            good_pairs += key_count[key_j]
            # Update the count for this key in the dictionary
            key_count[key_j] += 1

        # Calculate bad pairs by subtracting good pairs from total pairs
        return pairs - good_pairs