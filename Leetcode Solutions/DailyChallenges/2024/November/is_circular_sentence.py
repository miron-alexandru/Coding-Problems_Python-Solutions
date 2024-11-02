# problem link: https://leetcode.com/problems/circular-sentence/


# my solution:
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()

        # Single word in sentence: check if the first char and the last char match
        if len(words) == 1:
            return words[0][0] == words[0][-1]

        # For each word, compare the last char of the cur word with the first char
        # of the next, excluding the last word.
        for i in range(len(words) - 1):
            if words[i][-1] != words[i + 1][0]:
                return False

        # Compare last char of last word with first char of first word
        if words[-1][-1] != words[0][0]:
            return False

        return True
    
