# problem link: https://leetcode.com/problems/n-ary-tree-preorder-traversal


# my solution:
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # Define a function to traverse the tree recursively.
        def traverse(node):
            if node is None:
                return
            result.append(node.val)
            for child in node.children:
                traverse(child)
        # Store result
        result = []
        # perform a preorder traversal of the tree
        traverse(root)
        return result