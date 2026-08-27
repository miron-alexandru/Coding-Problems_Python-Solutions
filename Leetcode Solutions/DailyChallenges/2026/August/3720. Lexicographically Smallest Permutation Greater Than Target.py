# problem link:


# Description:
"""
You are given two strings s and target, both having length n, consisting of lowercase English letters.

Return the lexicographically smallest permutation of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.

A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.

 

Example 1:

Input: s = "abc", target = "bba"

Output: "bca"

Explanation:

The permutations of s (in lexicographical order) are "abc", "acb", "bac", "bca", "cab", and "cba".
The lexicographically smallest permutation that is strictly greater than target is "bca".
Example 2:

Input: s = "leet", target = "code"

Output: "eelt"

Explanation:

The permutations of s (in lexicographical order) are "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".
The lexicographically smallest permutation that is strictly greater than target is "eelt".
Example 3:

Input: s = "baba", target = "bbaa"

Output: ""

Explanation:

The permutations of s (in lexicographical order) are "aabb", "abab", "abba", "baab", "baba", and "bbaa".
None of them is lexicographically strictly greater than target. Therefore, the answer is "".
"""

# Solution:
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cur = dict(Counter(s))
        
        best_i = -1
        best_char = ''
        best_counts = None
        
        for i in range(n):
            t = target[i]
            # find smallest available character strictly greater than t
            cand_char = None
            for c in range(ord(t) + 1, ord('z') + 1):
                ch = chr(c)
                if cur.get(ch, 0) > 0:
                    cand_char = ch
                    break
            
            if cand_char is not None:
                best_i = i
                best_char = cand_char
                best_counts = dict(cur)  # snapshot of counts before consuming target i
            
            # try to extend the exact prefix match with target i
            if cur.get(t, 0) > 0:
                cur[t] -= 1
            else:
                break
        
        if best_i == -1:
            return ""
        
        prefix = target[:best_i]
        remaining = dict(best_counts)
        remaining[best_char] -= 1
        
        suffix_parts = []
        for c in range(ord('a'), ord('z') + 1):
            ch = chr(c)
            cnt = remaining.get(ch, 0)
            if cnt > 0:
                suffix_parts.append(ch * cnt)
        
        return prefix + best_char + ''.join(suffix_parts)