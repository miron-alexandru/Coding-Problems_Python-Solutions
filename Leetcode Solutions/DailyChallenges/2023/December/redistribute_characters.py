# problem link: https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal


# my solution:
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_count = {}
    
        for word in words:
            for char in word:
                char_count[char] = char_count.get(char, 0) + 1

        for count in char_count.values():
            if count % len(words) != 0:
                return False

        return True