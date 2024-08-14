# problem link: https://leetcode.com/problems/combination-sum-ii/


# my solution:
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path, res):
            if target == 0:
                res.append(path)
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                # Recursive call
                backtrack(i + 1, target - candidates[i], path + [candidates[i]], res)
        
        candidates.sort()
        res = []
        backtrack(0, target, [], res)
        return res