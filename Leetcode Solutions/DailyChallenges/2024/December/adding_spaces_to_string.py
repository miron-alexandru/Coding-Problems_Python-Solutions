# problem link: https://leetcode.com/problems/adding-spaces-to-a-string/


# my solution:
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        space_pointer = 0
        n = len(spaces)

        for i, char in enumerate(s):
            if space_pointer < n and i == spaces[space_pointer]:
                result.append(" ")
                space_pointer += 1
            result.append(char)
        
        return "".join(result)
