# problem link: https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/


# solution:
from collections import deque

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # Helper function to find the maximum cycle length in the graph
        def max_cycle_length(favorite: List[int]) -> int:
            n = len(favorite)
            visited = [False] * n  # Tracks visited employees
            max_cycle = 0  # Stores the maximum cycle length found
            
            for start in range(n):
                if visited[start]:
                    continue
                cycle_nodes = []  # Store nodes in the current cycle exploration
                current = start
                
                # Explore the graph starting from 'start' to find a cycle
                while not visited[current]:
                    cycle_nodes.append(current)
                    visited[current] = True
                    current = favorite[current]
                
                # Check if a cycle exists and calculate its length
                for index, node in enumerate(cycle_nodes):
                    if node == current:  # Found the start of the cycle
                        max_cycle = max(max_cycle, len(cycle_nodes) - index)
                        break
            
            return max_cycle

        # Helper function to calculate the maximum number of employees seated using topological sorting
        def max_chain_with_pairs(favorite: List[int]) -> int:
            n = len(favorite)
            in_degree = [0] * n  # Tracks in-degrees of nodes
            chain_length = [1] * n  # Stores the chain length ending at each node
            
            # Calculate in-degrees of each node
            for person in favorite:
                in_degree[person] += 1
            
            # Use a queue to perform topological sorting
            queue = deque(node for node, degree in enumerate(in_degree) if degree == 0)
            
            while queue:
                current = queue.popleft()
                chain_length[favorite[current]] = max(chain_length[favorite[current]], chain_length[current] + 1)
                in_degree[favorite[current]] -= 1
                
                # If the in-degree becomes zero, add the node to the queue
                if in_degree[favorite[current]] == 0:
                    queue.append(favorite[current])
            
            # Sum chain lengths for all pairs where both nodes are each other's favorites
            return sum(chain_length[i] for i, person in enumerate(favorite) if i == favorite[favorite[i]])

        # Return the maximum of either a single cycle or chains combined with cycles of length 2
        return max(max_cycle_length(favorite), max_chain_with_pairs(favorite))
