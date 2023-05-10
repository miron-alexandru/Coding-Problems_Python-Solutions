# Problem Link: https://leetcode.com/problems/binary-tree-inorder-traversal/


# My Solution:
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        # use recursion to traverse left and rigt subtrees
        result += self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)

        return result
