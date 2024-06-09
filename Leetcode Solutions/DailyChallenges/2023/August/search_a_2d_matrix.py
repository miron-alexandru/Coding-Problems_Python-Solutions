# problem link: https://leetcode.com/problems/search-a-2d-matrix


# my solution:
# using binary search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        
        while left <= right:
        	# Get the middle index
            mid = left + (right - left) // 2    
            # Convert 1D index to 2D and get value
            mid_value = matrix[mid // cols][mid % cols]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1  # Target is likely in the right half of the search range
            else:
                right = mid - 1  # Target is likely in the left half of the search range
        
        return False