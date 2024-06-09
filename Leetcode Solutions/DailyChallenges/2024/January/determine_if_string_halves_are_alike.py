# problem link: https://leetcode.com/problems/determine-if-string-halves-are-alike


# my solutions:

#1
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2
        vowels = "aeiouAEIOU"

        a_count = 0
        b_count = 0

        a = s[:mid]
        b = s[mid:]

        for i in a:
            if i in vowels:
                a_count += 1

        for j in b:
            if j in vowels:
                b_count += 1

        if a_count == b_count:
            return True

        return False


#2

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2
        vowels = "aeiouAEIOU"

        a_count = b_count = 0

        for i, char in enumerate(s):
            if char in vowels:
                if i < mid:
                    a_count += 1
                else:
                    b_count += 1

        return a_count == b_count


# 3

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        mid = len(s) // 2

        return sum(1 for char in s[:mid] if char in vowels) == sum(1 for char in s[mid:] if char in vowels)
