# Problem Link: https://leetcode.com/problems/symmetric-tree/


# My Solution:
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # define a recursive func
        def isMirror(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            # check if nodes are mirros of each other
            return (node1.val == node2.val and
                    isMirror(node1.left, node2.right) and
                    isMirror(node1.right, node2.left))
        
        return isMirror(root.left, root.right)
