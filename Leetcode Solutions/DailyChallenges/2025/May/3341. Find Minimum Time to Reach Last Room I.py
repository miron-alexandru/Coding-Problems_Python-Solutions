# problem link: https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/


# Description
"""
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.

 

Example 1:

Input: moveTime = [[0,4],[4,4]]

Output: 6

Explanation:

The minimum time required is 6 seconds.

At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in one second.
Example 2:

Input: moveTime = [[0,0,0],[0,0,0]]

Output: 3

Explanation:

The minimum time required is 3 seconds.

At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in one second.
At time t == 2, move from room (1, 1) to room (1, 2) in one second.
Example 3:

Input: moveTime = [[0,1],[1,2]]

Output: 3

 

Constraints:

2 <= n == moveTime.length <= 50
2 <= m == moveTime[i].length <= 50
0 <= moveTime[i][j] <= 109
"""

# Solution:
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows, cols = len(moveTime), len(moveTime[0])
        minArrivalTime = [[inf] * cols for _ in range(rows)]
        minArrivalTime[0][0] = 0
        
        priorityQueue = [(0, 0, 0)]  # (currentTime, row, col)
        directions = (-1, 0, 1, 0, -1)  # for pairwise
        
        while True:
            currentTime, row, col = heappop(priorityQueue)
            
            if row == rows - 1 and col == cols - 1:
                return currentTime
            
            if currentTime > minArrivalTime[row][col]:
                continue
            
            for dx, dy in pairwise(directions):
                newRow, newCol = row + dx, col + dy
                if 0 <= newRow < rows and 0 <= newCol < cols:
                    nextAvailableTime = max(moveTime[newRow][newCol], minArrivalTime[row][col]) + 1
                    if minArrivalTime[newRow][newCol] > nextAvailableTime:
                        minArrivalTime[newRow][newCol] = nextAvailableTime
                        heappush(priorityQueue, (nextAvailableTime, newRow, newCol))