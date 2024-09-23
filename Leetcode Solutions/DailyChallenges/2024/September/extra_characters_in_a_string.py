# problm link: https://leetcode.com/problems/extra-characters-in-a-string/


# solution:

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Convert the dictionary list to a set for O(1) lookups
        string_set = set(dictionary)
        n = len(s)
        # Initialize an array f to hold the minimum extra characters needed
        f = [0] * (n + 1)

        # Iterate through each position in the string
        for i in range(1, n + 1):
            # Start with the worst case: assume the last character is extra
            f[i] = f[i - 1] + 1
            # Check all substrings ending at position i
            for j in range(i):
                # If the substring s[j:i] is in the dictionary and 
                # using it reduces the count of extra characters
                if s[j:i] in string_set and f[j] < f[i]:
                    # Update f[i] to the minimum extra characters found
                    f[i] = f[j]

        return f[n]
