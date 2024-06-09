# problem link: https://leetcode.com/problems/reverse-words-in-a-string


# my solution:

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        # Split the string into words
        words = s.split()
        # Reverse the order of words
        words.reverse()
        # Join the reversed words using a single space
        reversed_string = ' '.join(words)

        return reversed_string