# Problem Link: https://www.hackerrank.com/challenges/30-binary-search-trees/problem


# My Solution:
def getHeight(self, root):
    if root is None:
        return -1

    left_height = self.getHeight(root.left)
    right_height = self.getHeight(root.right)

    return 1 + max(left_height, right_height)
