# problem link: https://leetcode.com/problems/string-compression-iii/


# solution (not mine):

class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0

        while i < len(word):
            # Get the current character
            c = word[i]
            # Count how many times it repeats consecutively
            count = 1
            while i + count < len(word) and word[i + count] == c and count < 9:
                count += 1

            # Append the count and character to the compressed result
            comp += str(count) + c

            # Move the index past this sequence of characters
            i += count

        return comp