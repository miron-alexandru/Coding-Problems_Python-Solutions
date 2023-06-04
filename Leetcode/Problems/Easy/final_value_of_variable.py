# problem link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/


# my solutions:
# 1
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for op in operations:
            if op == "++X" or op == "X++":
                X +=1
            else:
                X -= 1
        return X

# 2
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for op in operations:
            X += 1 if "++" in op else -1
        return X

# 3

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return operations.count("++X") + operations.count("X++") - operations.count("--X") - operations.count("X--")
