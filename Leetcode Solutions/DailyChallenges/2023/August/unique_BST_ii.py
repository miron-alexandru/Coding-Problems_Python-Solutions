# problem link: https://leetcode.com/problems/unique-binary-search-trees-ii/


# my solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate_trees_helper(start, end):
            # Base case: If the start is greater than the end, there are no values left to form a subtree
            # Return an empty subtree.
            if start > end:
                return [None]

            all_trees = []
            # Try all values from start to end as the root of the BST
            for i in range(start, end + 1):
                # Generate all possible left subtrees with values less than the current root value
                left_subtrees = generate_trees_helper(start, i - 1)
                # Generate all possible right subtrees with values greater than the current root value
                right_subtrees = generate_trees_helper(i + 1, end)

                # Combine all possible left and right subtrees with the current root value
                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)

            return all_trees

        # Call the helper function with the range of values from 1 to n.
        return generate_trees_helper(1, n)