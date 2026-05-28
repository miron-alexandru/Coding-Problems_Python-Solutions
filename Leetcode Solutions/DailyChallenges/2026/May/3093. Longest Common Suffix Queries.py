# problem link: https://leetcode.com/problems/longest-common-suffix-queries/


# Description:
"""
You are given two arrays of strings wordsContainer and wordsQuery.

For each wordsQuery[i], you need to find a string from wordsContainer that has the longest common suffix with wordsQuery[i]. If there are two or more strings in wordsContainer that share the longest common suffix, find the string that is the smallest in length. If there are two or more such strings that have the same smallest length, find the one that occurred earlier in wordsContainer.

Return an array of integers ans, where ans[i] is the index of the string in wordsContainer that has the longest common suffix with wordsQuery[i].

 

Example 1:

Input: wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]

Output: [1,1,1]

Explanation:

Let's look at each wordsQuery[i] separately:

For wordsQuery[0] = "cd", strings from wordsContainer that share the longest common suffix "cd" are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
For wordsQuery[1] = "bcd", strings from wordsContainer that share the longest common suffix "bcd" are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
For wordsQuery[2] = "xyz", there is no string from wordsContainer that shares a common suffix. Hence the longest common suffix is "", that is shared with strings at index 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
Example 2:

Input: wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"]

Output: [2,0,2]

Explanation:

Let's look at each wordsQuery[i] separately:

For wordsQuery[0] = "gh", strings from wordsContainer that share the longest common suffix "gh" are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6.
For wordsQuery[1] = "acbfgh", only the string at index 0 shares the longest common suffix "fgh". Hence it is the answer, even though the string at index 2 is shorter.
For wordsQuery[2] = "acbfegh", strings from wordsContainer that share the longest common suffix "gh" are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6.
"""

# Solution:
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        # For each node: children dict, best_idx (index in wordsContainer with
        # shortest length / earliest position among all words passing through)
        trie = {}

        def best(a, b):
            """Return the better container index: shorter word wins earlier index breaks ties."""
            if a is None:
                return b
            la, lb = len(wordsContainer[a]), len(wordsContainer[b])
            if lb < la or (lb == la and b < a):
                return b
            return a

        # Insert reversed wordsContainer strings
        for idx, word in enumerate(wordsContainer):
            node = trie
            # Update root's best candidate before descending
            node.setdefault("best", None)
            node["best"] = best(node["best"], idx)

            for ch in reversed(word):
                node = node.setdefault(ch, {})
                node.setdefault("best", None)
                node["best"] = best(node["best"], idx)

        # walk reversed query as far as possible and return best at last node
        ans = []
        for word in wordsQuery:
            node = trie
            for ch in reversed(word):
                if ch not in node:
                    break
                node = node[ch]
            ans.append(node["best"])

        return ans

