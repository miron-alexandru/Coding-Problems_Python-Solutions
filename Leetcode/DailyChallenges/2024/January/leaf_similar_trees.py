# problem link: https://leetcode.com/problems/leaf-similar-trees


# my solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Helper function to retrieve leaf nodes of a tree and store them in a list
        def get_leaf_nodes(root, leaf_list):
            # If the current node is a leaf append its value to the leaf list
            if not root.left and not root.right:
                leaf_list.append(root.val)
            # Recursively process the left subtree if it exists
            if root.left:
                get_leaf_nodes(root.left, leaf_list)
            # Recursively process the right subtree if it exists
            if root.right:
                get_leaf_nodes(root.right, leaf_list)

        # Helper function to check if the leaf nodes of two trees are the same
        def same_leafs(root1, root2):
            leaf_list1, leaf_list2 = [], []
            
            # Populate leaf_list1 with leaf nodes of the first tree
            get_leaf_nodes(root1, leaf_list1)
            
            # Populate leaf_list2 with leaf nodes of the second tree
            get_leaf_nodes(root2, leaf_list2)
            
            return leaf_list1 == leaf_list2

        return same_leafs(root1, root2)