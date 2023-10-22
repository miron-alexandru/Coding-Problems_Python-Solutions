# problem link: https://leetcode.com/problems/pascals-triangle-ii



# my solution:
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        curr_row = [1]

        for row_number in range(1, rowIndex + 1):
            new_row = [1]

            for j in range(1, len(curr_row)):
                new_element = curr_row[j - 1] + curr_row[j]
                new_row.append(new_element)

            curr_row = new_row
            new_row.append(1)

        return curr_row


        




