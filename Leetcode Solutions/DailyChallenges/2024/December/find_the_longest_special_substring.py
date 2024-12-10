# problem link: https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/


# my solution:
class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return -1

        # Helper function to check if a substring is special.
        def is_special(sub):
            return all(c == sub[0] for c in sub)

        # count occurrences of substrings
        substring_counts = {}

        # Generate all substrings
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                if is_special(sub):
                    if sub not in substring_counts:
                        substring_counts[sub] = 0
                    substring_counts[sub] += 1
                else:
                    break

        # Filter substrings that appear at least three times
        valid_substrings = {sub: count for sub, count in substring_counts.items() if count >= 3}

        if not valid_substrings:
            return -1

        # Find the longest valid substring
        max_length = max(len(sub) for sub in valid_substrings.keys())
        return max_length