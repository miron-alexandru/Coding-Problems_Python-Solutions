# problem link: https://leetcode.com/problems/min-cost-climbing-stairs

# my solution:
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        minCost = [0] * n
        
        # Base cases
        minCost[0] = cost[0]
        minCost[1] = cost[1]
        
        # Calculate minimum cost for each step
        for i in range(2, n):
            minCost[i] = cost[i] + min(minCost[i-1], minCost[i-2])
        
        return min(minCost[n-1], minCost[n-2])