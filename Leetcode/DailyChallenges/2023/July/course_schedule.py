# problem link: https://leetcode.com/problems/course-schedule/


# my solution:
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        # Create the visited array
        visited = [0] * numCourses

        # DFS traversal
        def dfs(course):
            # Mark the current course as visited
            visited[course] = 1

            # Check the courses that depend on the current course
            for dependent in graph[course]:
                if visited[dependent] == 1:
                    return False  # Cycle detected
                elif visited[dependent] == 0 and not dfs(dependent):
                    return False

            visited[course] = 2  # Mark the course as completely visited
            return True

        # Iterate through each course and perform DFS if unvisited
        for course in range(numCourses):
            if visited[course] == 0 and not dfs(course):
                return False

        return True