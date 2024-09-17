# problem link; https://leetcode.com/problems/uncommon-words-from-two-sentences/



# my solution:

from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split sentences into words
        words1 = s1.split()
        words2 = s2.split()
        
        # Count occurrences of each word
        count = Counter(words1 + words2)
        
        # Find uncommon words
        uncommon_words = [word for word in count if count[word] == 1]
        
        return uncommon_words
