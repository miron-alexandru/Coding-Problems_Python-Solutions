# problem link: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/



# my solution:
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        
        # Calculate moves from left to right
        count = 0  # Number of balls encountered so far
        moves = 0  # Total moves for left to current index
        for i in range(n):
            answer[i] += moves
            if boxes[i] == '1':
                count += 1
            moves += count
        
        # Calculate moves from right to left
        count = 0  # Reset count for balls
        moves = 0  # Total moves for right to current index
        for i in range(n - 1, -1, -1):
            answer[i] += moves
            if boxes[i] == '1':
                count += 1
            moves += count
        
        return answer
