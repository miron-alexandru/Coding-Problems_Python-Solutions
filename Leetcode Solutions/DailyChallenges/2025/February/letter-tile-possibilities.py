# problem link: https://leetcode.com/problems/letter-tile-possibilities/


# my solution:
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(counter):
            nonlocal count
            for char in counter:
                if counter[char] > 0:
                    count += 1  # Count the new sequence
                    counter[char] -= 1  # Use this letter
                    backtrack(counter)  # Recurse
                    counter[char] += 1  # Backtrack

        count = 0
        backtrack(Counter(tiles))
        return count
