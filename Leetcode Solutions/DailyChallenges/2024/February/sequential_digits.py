# problem link: 	https://leetcode.com/problems/sequential-digits/


# my solution:
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        
        for start_digit in range(1, 9):
            num = start_digit
            next_digit = start_digit + 1
            
            while num <= high and next_digit <= 9:
                num = num * 10 + next_digit
                if low <= num <= high:
                    result.append(num)
                next_digit += 1

        return sorted(result)