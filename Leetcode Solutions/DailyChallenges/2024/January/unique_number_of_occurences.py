# problem link: https://leetcode.com/problems/unique-number-of-occurrences



# my solution:
from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = defaultdict(int)
        
        for i in arr:
            occurrences[i] += 1
        
        counts_seen = set()
        return all(occurrence not in counts_seen and counts_seen.add(occurrence) is None for occurrence in occurrences.values())
