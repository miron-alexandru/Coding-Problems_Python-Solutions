# problem link: https://leetcode.com/problems/can-place-flowers


# my solution:
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                count += 1
                i += 2  # skip the next plot since it cannot be planted on
            else:
                i += 1
            
            if count >= n:
                return True
        
        return False
