# problem link: https://leetcode.com/problems/ipo/



# my solution:
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        # Create a list of tuples where each tuple is: capital required, profit
        projects = [(capital[i], profits[i]) for i in range(n)]
        # Sort projects by the capital required
        projects.sort()

        # use max-heap to store the profits of projects we can afford
        max_heap = []
        # Initialize current capital with the initial capital and index to iterate
        # through the projects
        current_capital = w
        project_index = 0

        # Iterate up to k times to select at most k projects
        for _ in range(k):
            # Add all projects that can be started with the current capital to the max-heap
            while project_index < n and projects[project_index][0] <= current_capital:
                # Push the negative profit to simulate a max-heap
                heapq.heappush(max_heap, -projects[project_index][1])
                project_index += 1

            # If there are no projects that can be started, break the loop
            if not max_heap:
                break

            # Pop the project with the maximum profit from the heap
            current_capital += -heapq.heappop(max_heap)

        return current_capital
