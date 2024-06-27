# problem link: https://leetcode.com/problems/find-center-of-star-graph/



# my solution:
from collections import Counter

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Keep track of the frequency of each node
        nodes_counter = Counter()

        for edge in edges:
            # Unpack the edge to get the two nodes ui and vi
            ui, vi = edge
            # Increment the count for node ui and node vi
            nodes_counter[ui] += 1
            nodes_counter[vi] += 1
        # Find the node with the highest frequency
        for node, count in nodes_counter.items():
            # The center node of the star graph will have a count equal to the number of edges
            if count == len(edges):
                return node