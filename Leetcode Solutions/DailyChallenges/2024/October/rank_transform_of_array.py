# problem link: https://leetcode.com/problems/rank-transform-of-an-array


# my solution:
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        rank_map = {num: rank + 1 for rank, num in enumerate(sorted_unique)} 

        return [rank_map[num] for num in arr]