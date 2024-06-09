<<<<<<< HEAD
# problem link: https://leetcode.com/problems/valid-anagram



# my solution:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency = {}
        for c in s:
            frequency[c] = frequency.get(c, 0) + 1

        for c in t:
            frequency[c] = frequency.get(c, 0) - 1
            if frequency[c] < 0:
                return False

        return True
=======
# problem link: https://leetcode.com/problems/valid-anagram


# my solution:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency = {}
        for c in s:
            frequency[c] = frequency.get(c, 0) + 1

        for c in t:
            frequency[c] = frequency.get(c, 0) - 1
            if frequency[c] < 0:
                return False

        return True
>>>>>>> e83eac39866bad2b88e736d6915419678d38c8a7
