# problem link: https://leetcode.com/problems/robot-return-to-origin

# my solutions:
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for move in moves:
            if move is 'R':
                x += 1
            elif move is 'L':
                x -= 1
            elif move is 'U':
                y += 1
            else:
                y -= 1

        return x == y == 0


# other solution:
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')