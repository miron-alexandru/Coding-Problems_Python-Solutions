# problem link: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix


# my solution:
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Calculate the strength of each row
        rows_strength = [(i, sum(row)) for i, row in enumerate(mat)]
        # Sort the rows_strength list
        rows_strength.sort(key=lambda x: (x[1], x[0]))
        # indices of the k weakest rows
        weakest_indices = [x[0] for x in rows_strength[:k]]
        
        return weakest_indices