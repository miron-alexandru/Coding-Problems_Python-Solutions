# problem link: https://leetcode.com/problems/sort-the-people/

# my solution:
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sorted_names = [name for _, name in sorted(zip(heights, names), reverse=True)]
        return sorted_names