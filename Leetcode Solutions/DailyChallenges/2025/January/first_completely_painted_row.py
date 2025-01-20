# problem link: https://leetcode.com/problems/first-completely-painted-row-or-column/



# my solution:
class Solution:
        def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
            m, n = len(mat), len(mat[0])
        
            # Preprocess positions of each value in the matrix
            positions = {}
            for i in range(m):
                for j in range(n):
                    positions[mat[i][j]] = (i, j)
            
            # Frequency counters for rows and columns
            row_count = [0] * m
            col_count = [0] * n
            
            # Traverse arr and update row and column counts
            for i, num in enumerate(arr):
                r, c = positions[num]
                row_count[r] += 1
                col_count[c] += 1
                
                # Check if the row or column is fully painted
                if row_count[r] == n or col_count[c] == m:
                    return i
            
            return -1
