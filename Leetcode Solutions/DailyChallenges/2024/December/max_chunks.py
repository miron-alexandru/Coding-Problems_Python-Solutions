# problem link: https://leetcode.com/problems/max-chunks-to-make-sorted/


# my solution:
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_so_far = 0
        chunks = 0

        for i, value in enumerate(arr):
            max_so_far = max(max_so_far, value)
            if max_so_far == i:
                chunks += 1

        return chunks