# problem link: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/



# my solution:
from collections import defaultdict
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = defaultdict(int)
        result = []
        total = 0
        n = len(A)

        for i in range(n):
            freq[A[i]] += 1
            freq[B[i]] += 1

            if freq[A[i]] == 2:
                total += 1
            if freq[B[i]] == 2 and A[i] != B[i]:
                total += 1

            result.append(total)

        return result

