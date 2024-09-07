# problem link: https://leetcode.com/problems/linked-list-in-binary-tree/


# my solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        # Helper function to match the list with the downward path
        def dfs(treeNode, listNode):
            # If the linked list is fully traversed, we found a match
            if not listNode:
                return True
            # If the tree node is null, no path exists
            if not treeNode:
                return False
            # Check if the current values match and move to the next in both the list and the tree
            if treeNode.val == listNode.val:
                return dfs(treeNode.left, listNode.next) or dfs(treeNode.right, listNode.next)
            return False
        
        # We need to try starting from every node in the tree
        def traverse(treeNode):
            # If no tree node, return False
            if not treeNode:
                return False
            # Either we found the path starting here, or we look for other nodes in the tree
            return dfs(treeNode, head) or traverse(treeNode.left) or traverse(treeNode.right)
        
        return traverse(root)

