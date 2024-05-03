# problem link: https://leetcode.com/problems/reverse-prefix-of-word


# my solution:
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        if index != -1:
            return word[:index+1][::-1] + word[index+1:]
        else:
            return word