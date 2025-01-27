# problem link: https://leetcode.com/problems/course-schedule-iv/



# solution:
from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Create an adjacency list for the graph
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)
        
        # Use a matrix to store reachability
        isReachable = [[False] * numCourses for _ in range(numCourses)]
        
        # Perform BFS for each course to find all reachable courses
        for i in range(numCourses):
            queue = deque([i])
            while queue:
                course = queue.popleft()
                for neighbor in graph[course]:
                    if not isReachable[i][neighbor]:
                        isReachable[i][neighbor] = True
                        queue.append(neighbor)
        
        # Answer queries using the isReachable matrix
        result = []
        for u, v in queries:
            result.append(isReachable[u][v])
        
        return result
