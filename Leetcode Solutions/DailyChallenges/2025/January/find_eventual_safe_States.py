# problem link: https://leetcode.com/problems/find-eventual-safe-states/


# solution:
from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = [[] for _ in range(n)]
        in_degree = [0] * n

        # Build the reverse graph and calculate in-degrees
        for node in range(n):
            for neighbor in graph[node]:
                reverse_graph[neighbor].append(node)
                in_degree[node] += 1

        # Initialize the queue with all terminal nodes (in-degree 0)
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        safe_nodes = []

        while queue:
            current = queue.popleft()
            safe_nodes.append(current)
            for neighbor in reverse_graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted(safe_nodes)
