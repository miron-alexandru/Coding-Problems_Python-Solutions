# problem link: https://leetcode.com/problems/validate-stack-sequences/


# my solution:
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for num in pushed:
            stack.append(num)
            # if stack is not empty and the top element of the stack
            # equals the current element, pop the top element from the stack and
            # increment the index for the popped list
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack
