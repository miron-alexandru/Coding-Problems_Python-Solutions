# problem link:  https://leetcode.com/problems/assign-cookies


# my solution:

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        i, j = 0, 0
        content_children = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                content_children += 1
                i += 1
            j += 1

        return content_children
