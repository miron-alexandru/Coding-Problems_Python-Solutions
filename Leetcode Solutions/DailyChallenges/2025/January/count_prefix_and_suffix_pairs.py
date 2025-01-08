# problem link: https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/


# my solution:
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0

        def isPrefixAndSuffix(str1, str2):
            if len(str1) > len(str2):
                return False

            return str2[:len(str1)] == str1 and str2[-len(str1):] == str1

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1

        return count

        