# problem link: https://leetcode.com/problems/word-subsets/


# my solution:
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
    	# Function to check if a word is universal
        def is_universal(word, max_freq):
            freq = Counter(word)
            for char, count in max_freq.items():
                if freq[char] < count:
                    return False
            return True

        max_freq = Counter()

        # compute maximum frequencies
        for word in words2:
            freq = Counter(word)
            for char in freq:
                max_freq[char] = max(max_freq[char], freq[char])

        universal_words = [word for word in words1 if is_universal(word, max_freq)]

        return universal_words


