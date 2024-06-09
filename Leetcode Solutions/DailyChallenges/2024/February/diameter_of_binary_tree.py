# problem link: https://leetcode.com/problems/diameter-of-binary-tree/submissions/


# my solution:
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height_and_diameter(node):
            if node is None:
                return 0, 0

            left_height, left_diameter = height_and_diameter(node.left)
            right_height, right_diameter = height_and_diameter(node.right)

            current_height = 1 + max(left_height, right_height)
            current_diameter = max(left_height + right_height, left_diameter, right_diameter)

            return current_height, current_diameter

        _, diameter = height_and_diameter(root)
        return diameter
