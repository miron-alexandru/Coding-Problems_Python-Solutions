# problem link: https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/



# solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        self.recover_tree(root, 0)

    def recover_tree(self, node: Optional[TreeNode], val: int):
        if not node:
            return
        node.val = val
        self.values.add(val)
        self.recover_tree(node.left, 2 * val + 1)
        self.recover_tree(node.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.values
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)