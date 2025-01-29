# problem link: https://leetcode.com/problems/redundant-connection/


# my solution:
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Initialize parent array
        parent = [i for i in range(len(edges) + 1)]
        
        # Find function with path compression
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        
        # Union function
        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u == root_v:
                return False  # Cycle detected
            parent[root_v] = root_u
            return True
        
        # Iterate through edges
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        
        return []  # No redundant edge found