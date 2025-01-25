# problem link: https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/



# solution:
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        
        # Pair each number with its index and sort the array by the number values
        sorted_nums_with_indices = sorted(zip(nums, range(n)))
        
        # Initialize the result array with zeros
        result = [0] * n
        
        i = 0
        while i < n:
            # Find the range of numbers that belong to the same connected component
            j = i + 1
            while j < n and sorted_nums_with_indices[j][0] - sorted_nums_with_indices[j - 1][0] <= limit:
                j += 1
            
            # Extract the indices of the connected component and sort them
            connected_indices = sorted(index for _, index in sorted_nums_with_indices[i:j])
            
            # Assign the values to the result array in lexicographical order
            for sorted_index, (value, _) in zip(connected_indices, sorted_nums_with_indices[i:j]):
                result[sorted_index] = value
            
            # Move to the next connected component
            i = j
        
        return result
