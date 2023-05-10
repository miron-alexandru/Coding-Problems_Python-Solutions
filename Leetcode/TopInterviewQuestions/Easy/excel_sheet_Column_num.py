# problem link: https://leetcode.com/problems/excel-sheet-column-number/


# my solution:
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # init the result var to 0
        result = 0
        # loop through each char in the column title str
        for char in columnTitle:
            # get the numeric value of the current character
            value = ord(char) - 64
            # update the result variable by multiplying it by 26
            # and adding the numeric value of the current char
            result = result * 26 + value
        return result
