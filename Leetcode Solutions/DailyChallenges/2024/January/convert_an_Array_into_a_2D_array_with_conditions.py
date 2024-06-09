# problem link: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions



# my solution:
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort(reverse=True)
    
        # Initialize an empty list to store the result
        result = []

        for num in nums:
            # For each element check if it can be added to an existing row
            added = False
            for row in result:
                # If the element is not already in the row add it and break the loop
                if num not in row:
                    row.append(num)
                    added = True
                    break
            
            # If the element couldn't be added to any existing row create a new row
            if not added:
                result.append([num])

        return result