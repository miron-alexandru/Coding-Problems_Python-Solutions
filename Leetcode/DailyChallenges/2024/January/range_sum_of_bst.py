# problem link: https://leetcode.com/problems/range-sum-of-bst/


# my solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        curr_sum = 0

        # Base case: If the root is None (empty tree), return 0
        if root == None:
            return 0

        # Initialize a deque for level-order traversal
        q = deque()

        q.append(root)

        # Perform level-order traversal using the queue
        while len(q) > 0:
            # Dequeue the leftmost node in the current level
            curr = q.popleft()

            # Check if the value of the current node is within the specified range
            if curr.val >= low and curr.val <= high:
                curr_sum += curr.val

            # Enqueue the left child if it exists and its value is greater than the lower bound
            if curr.left != None and curr.val > low:
                q.append(curr.left)

            # Enqueue the right child if it exists and its value is less than the upper bound
            if curr.right != None and curr.val < high:
                q.append(curr.right)

        return curr_sum
