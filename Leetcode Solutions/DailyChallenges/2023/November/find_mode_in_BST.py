# problem link: https://leetcode.com/problems/find-mode-in-binary-search-tree


# my solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def inOrderTraversal(node):
            if not node:
                return

            inOrderTraversal(node.left)
            freq_dict[node.val] += 1
            inOrderTraversal(node.right)

        freq_dict = defaultdict(int)
        inOrderTraversal(root)

        max_freq = max(freq_dict.values())
        modes = [key for key, value in freq_dict.items() if value == max_freq]

        return modes