# problem link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

# my solution:
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        left = 0
        right = k
        max_count = 0
        count = sum(1 for c in s[left:right] if c in vowels)
        max_count = count

        while right < len(s):
            if s[left] in vowels:
                count -= 1
            if s[right] in vowels:
                count += 1
            max_count = max(max_count, count)
            left += 1
            right += 1

        return max_count