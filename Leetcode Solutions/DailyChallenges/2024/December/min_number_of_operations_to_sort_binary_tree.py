# problem link: https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/


# solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def level_order_traversal(root: TreeNode) -> List[List[int]]:
            """Perform level-order traversal and collect nodes at each level."""
            levels = []
            queue = deque([root])
            while queue:
                level_size = len(queue)
                level = []
                for _ in range(level_size):
                    node = queue.popleft()
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                levels.append(level)
            return levels

        def min_swaps_to_sort(arr: List[int]) -> int:
            """Calculate the minimum swaps to sort the array."""
            n = len(arr)
            sorted_arr = sorted((val, idx) for idx, val in enumerate(arr))
            visited = [False] * n
            swaps = 0
            
            for i in range(n):
                if visited[i] or sorted_arr[i][1] == i:
                    continue
                
                # Count the size of the cycle
                cycle_size = 0
                x = i
                while not visited[x]:
                    visited[x] = True
                    x = sorted_arr[x][1]
                    cycle_size += 1
                
                if cycle_size > 1:
                    swaps += cycle_size - 1
            
            return swaps

        # Perform level-order traversal
        levels = level_order_traversal(root)

        # Calculate total minimum swaps
        total_swaps = 0
        for level in levels:
            total_swaps += min_swaps_to_sort(level)

        return total_swaps