# problem link: https://leetcode.com/problems/number-of-provinces


# my solution:
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = 0
        visited = [False] * n

        for city in range(n):
            if not visited[city]:
                queue = [city]
                while queue:
                    current_city = queue.pop(0)
                    visited[current_city] = True
                    for neighbor in range(n):
                        if isConnected[current_city][neighbor] == 1 and not visited[neighbor]:
                            queue.append(neighbor)
                provinces += 1

        return provinces