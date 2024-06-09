# problem link: https://leetcode.com/problems/find-the-town-judge



# my solution:
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count = [0] * (n + 1)
        trusted_count = [0] * (n + 1)
        
        # Iterate through trust relationships and update counts
        for a, b in trust:
            trust_count[a] += 1
            trusted_count[b] += 1
        
        # Iterate through people to find the town judge
        for i in range(1, n + 1):
            if trust_count[i] == 0 and trusted_count[i] == n - 1:
                return i
        
        return -1
