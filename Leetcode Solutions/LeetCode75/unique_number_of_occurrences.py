# problem link: https://leetcode.com/problems/unique-number-of-occurrences


# my solution:
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}
        for i in arr:
            if i in occurrences:
                occurrences[i] += 1
            else:
                occurrences[i] = 1

        counts_seen = set()
        for count in occurrences.values():
            if count in counts_seen:
                return False
            counts_seen.add(count)

        return True
