# problem link: https://leetcode.com/problems/excel-sheet-column-title/


# my solution:
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""
    
        while columnNumber > 0:
            # Adjusting the column number to be 0-indexed
            columnNumber -= 1
            
            # Get the remainder when divided by 26 (digits 0-25)
            remainder = columnNumber % 26
            
            # Convert the remainder to its corresponding character
            title = chr(65 + remainder) + title
            
            # Divide the column number by 26 to move to the next digit
            columnNumber //= 26
        
        return title