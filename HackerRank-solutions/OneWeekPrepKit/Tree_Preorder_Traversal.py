# problem link: https://www.hackerrank.com/challenges/one-week-preparation-kit-tree-preorder-traversal/problem


# My Solution:


def preOrder(root):
    if root:
        print(root.info, end=" ")
        # recursively call the func on the left and right child
        preOrder(root.left)
        preOrder(root.right)
