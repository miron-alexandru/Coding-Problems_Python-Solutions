# problem link: https://leetcode.com/problems/find-the-punishment-number-of-an-integer


# solution:
class Solution:
    def punishmentNumber(self, n: int) -> int:
        # Helper function to check if the number can be split in a way that
        # the sum of the parts equals the target value
        def check(number_str: str, start_index: int, target_sum: int) -> bool:
            length = len(number_str)
            
            # If the starting index exceeds or reaches the length of the number,
            # check if the remaining sum is zero (success condition).
            if start_index >= length:
                return target_sum == 0
            
            current_value = 0
            for current_index in range(start_index, length):
                # Construct the current part by adding the next digit
                current_value = current_value * 10 + int(number_str[current_index])
                
                # If the current part exceeds the target sum, stop the loop
                if current_value > target_sum:
                    break
                
                # Recursively check the remaining part with the reduced target sum
                if check(number_str, current_index + 1, target_sum - current_value):
                    return True
            return False
        
        total_sum = 0
        # Iterate through all numbers from 1 to n
        for i in range(1, n + 1):
            square_value = i * i
            # Check if the square of the current number can be split into parts that sum to the number
            if check(str(square_value), 0, i):
                total_sum += square_value
        
        return total_sum
