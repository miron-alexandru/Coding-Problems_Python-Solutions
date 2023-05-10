# Problem Link: https://www.hackerrank.com/challenges/bfsshortreach/problem

# Solution: (not mine)
from collections import deque


def bfs(n, m, edges, s):
    adj_list = [[] for i in range(n)]
    for edge in edges:
        u, v = edge
        adj_list[u - 1].append(v - 1)
        adj_list[v - 1].append(u - 1)

    distances = [-1] * n

    # Initialize queue with starting node
    queue = deque([s - 1])
    distances[s - 1] = 0

    # BFS algorithm
    while queue:
        u = queue.popleft()
        for v in adj_list[u]:
            if distances[v] == -1:
                distances[v] = distances[u] + 6
                queue.append(v)

    # Return distances to nodes (except starting node)
    return [dist for i, dist in enumerate(distances) if i != s - 1]
