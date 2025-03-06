# problem link: https://leetcode.com/problems/find-missing-and-repeated-values/



# solution:
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        size = n * n  # Total numbers in the grid
        frequency = [0] * (size + 1)  # Frequency array to track occurrences
        
        # Count occurrences of each number
        for row in grid:
            for num in row:
                frequency[num] += 1
        
        missing = repeated = 0
        
        # Identify the missing and repeated numbers
        for num in range(1, size + 1):
            if frequency[num] == 2:
                repeated = num
            elif frequency[num] == 0:
                missing = num
        
        return [repeated, missing]
