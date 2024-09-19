# problem link: https://leetcode.com/problems/different-ways-to-add-parentheses/


# my solution:
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Cache results of subexpressions to avoid recomputation
        memo = {}
        
        def compute(expr: str) -> List[int]:
            if expr in memo:
                return memo[expr]
            
            results = []
            for i, char in enumerate(expr):
                if char in '+-*':
                    # Divide the expression into left and right subexpressions
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])
                    
                    # Combine results from left and right subexpressions
                    for l in left:
                        for r in right:
                            if char == '+':
                                results.append(l + r)
                            elif char == '-':
                                results.append(l - r)
                            elif char == '*':
                                results.append(l * r)
            
            # If the expression is just a number return it as an integer
            if not results:
                results = [int(expr)]
            
            memo[expr] = results
            return results
        
        return compute(expression)
