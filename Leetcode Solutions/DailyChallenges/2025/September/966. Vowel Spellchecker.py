# problem link: https://leetcode.com/problems/vowel-spellchecker/


# Solution:
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact = set(wordlist)
        caseMap = {}
        vowelMap = {}

        for w in wordlist:
            lower = w.lower()
            devowel = self.deVowel(lower)
            if lower not in caseMap:
                caseMap[lower] = w
            if devowel not in vowelMap:
                vowelMap[devowel] = w

        result = []
        for q in queries:
            if q in exact:
                result.append(q)
            else:
                lower = q.lower()
                devowel = self.deVowel(lower)
                if lower in caseMap:
                    result.append(caseMap[lower])
                elif devowel in vowelMap:
                    result.append(vowelMap[devowel])
                else:
                    result.append("")
        return result

    def deVowel(self, s):
        return ''.join('*' if c in 'aeiou' else c for c in s)

        def solve(query):
            if query in words_perfect:
                return query

            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]

            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ""

        return map(solve, queries)