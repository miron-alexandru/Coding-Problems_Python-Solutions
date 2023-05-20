# problem link: https://leetcode.com/problems/baseball-game


# my solution:
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        
        for op in operations:
            if op == '+':
                scores.append(scores[-1] + scores[-2])
            elif op == 'D':
                scores.append(2 * scores[-1])
            elif op == 'C':
                scores.pop()
            else:
                scores.append(int(op))
        
        return sum(scores)
