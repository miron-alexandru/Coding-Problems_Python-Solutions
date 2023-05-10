# Problem Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/


# My Solution:
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # define a recursive func
        def createTree(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            # recursively build the left and right subtrees
            root.left = createTree(left, mid - 1)
            root.right = createTree(mid + 1, right)
            return root

        return createTree(0, len(nums) - 1)
