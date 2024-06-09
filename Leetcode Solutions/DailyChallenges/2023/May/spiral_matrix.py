# problem link: https://leetcode.com/problems/spiral-matrix/


# my solution:
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []

        result = []

        while matrix:
            # Traverse top row
            result.extend(matrix.pop(0))

            # Traverse right column
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())

            # Traverse bottom row
            if matrix and matrix[-1]:
                result.extend(matrix.pop()[::-1])

            # Traverse left column
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))

        return result