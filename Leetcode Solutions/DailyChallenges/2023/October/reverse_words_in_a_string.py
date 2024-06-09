# problem link: https://leetcode.com/problems/reverse-words-in-a-string-iii



# my solution:
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        # reverse each word and join back with spaces
        reversed_words = [word[::-1] for word in words]
        reversed_sentence = ' '.join(reversed_words)

        return reversed_sentence