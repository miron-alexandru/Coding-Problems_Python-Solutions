# problem link: https://leetcode.com/problems/pass-the-pillow/


# my solution:
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = 1
        index = 1

        for i in range(time):
            index += direction

            if index == n:
                direction = -1
            elif index == 1:
                direction = 1

        return index