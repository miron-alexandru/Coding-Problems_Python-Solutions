# problem link: https://leetcode.com/problems/lemonade-change/



# my solution:
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5, count10 = 0, 0
        for b in bills:
            if b == 5:
                count5 += 1
            elif b == 10:
                if count5 > 0:
                    count5 -= 1
                    count10 += 1
                else:
                    return False
            elif b == 20:
                if count10 > 0 and count5 > 0:
                    count10 -= 1
                    count5 -= 1
                elif count5 >= 3:
                    count5 -= 3
                else:
                    return False
        return True