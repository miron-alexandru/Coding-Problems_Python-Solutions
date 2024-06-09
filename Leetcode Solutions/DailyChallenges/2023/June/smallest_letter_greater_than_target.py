# problem link: https://leetcode.com/problems/find-smallest-letter-greater-than-target


# my solutions:

# brute force:

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for char in letters:
            if char > target:
                return char
        return letters[0]


# binary search:
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        result = letters[0]

        while left <= right:
            mid = left + (right - left) // 2

            if letters[mid] > target:
                result = letters[mid]
                right = mid - 1
            else:
                left = mid + 1

        return result


# using the bisect module:
import bisect

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect.bisect_right(letters, target)
        return letters[index % len(letters)]