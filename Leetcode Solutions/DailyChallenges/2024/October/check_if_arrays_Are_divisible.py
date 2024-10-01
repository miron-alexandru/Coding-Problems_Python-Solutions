# problem link: https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/


# my solution:

from collections import defaultdict

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = defaultdict(int)
        
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1
        
        for remainder in list(remainder_count.keys()):
            # Remainder 0 case: must have an even count to form pairs
            if remainder == 0:
                if remainder_count[remainder] % 2 != 0:
                    return False
            
            # Other remainders must have corresponding count with their complement k - remainder
            elif remainder_count[remainder] != remainder_count[k - remainder]:
                return False
        
        return True
