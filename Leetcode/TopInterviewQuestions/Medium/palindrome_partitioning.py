# Problem link: https://leetcode.com/problems/palindrome-partitioning/


# my solution:
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # define two funcs, palindrome and backtrack
        def palindrome(string):
            return string == string[::-1]

        def backtrack(start, path):
            if start == len(s):
                partitions.append(path[:])
                return

            for i in range(start, len(s)):
                substring = s[start : i + 1]
                if palindrome(substring):
                    path.append(substring)
                    backtrack(i + 1, path)
                    path.pop()

        partitions = []
        backtrack(0, [])
        return partitions
