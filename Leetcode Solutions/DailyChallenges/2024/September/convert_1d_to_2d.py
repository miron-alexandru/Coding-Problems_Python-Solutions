# problem link: https://leetcode.com/problems/convert-1d-array-into-2d-array/



# my solution:
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != n * m:
            return []

        result = []
    
        # Iterate over the number of rows
        for i in range(m):
            # Extract the sublist for the current row
            row = original[i * n:(i + 1) * n]
            result.append(row)
        
        return result