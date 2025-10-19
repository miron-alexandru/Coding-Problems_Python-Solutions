# problem link: https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/


# Description:
"""
You are given a string s of even length consisting of digits from 0 to 9, and two integers a and b.

You can apply either of the following two operations any number of times and in any order on s:

Add a to all odd indices of s (0-indexed). Digits post 9 are cycled back to 0. For example, if s = "3456" and a = 5, s becomes "3951".
Rotate s to the right by b positions. For example, if s = "3456" and b = 1, s becomes "6345".
Return the lexicographically smallest string you can obtain by applying the above operations any number of times on s.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example, "0158" is lexicographically smaller than "0190" because the first position they differ is at the third letter, and '5' comes before '9'.
"""


# Solution:
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # Queue for BFS
        q = deque([s])
        # Visited set to avoid repeats
        seen = {s}
        res = s  # Track smallest found so far

        while q:
            cur = q.popleft()
            # Update smallest string
            if cur < res:
                res = cur

            # add a to all odd indices
            chars = list(cur)
            for i in range(1, len(chars), 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            added = ''.join(chars)

            # rotate right by b
            rotated = cur[-b:] + cur[:-b]

            # Enqueue new strings if unseen
            for nxt in (added, rotated):
                if nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)

        return res
