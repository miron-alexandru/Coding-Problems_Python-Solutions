# problem link: https://leetcode.com/problems/string-matching-in-an-array/



# my solution:
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        result = []

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    result.append(words[i])
                    break 
        
        return result
