# problem link: https://leetcode.com/problems/height-checker


# my solution:
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Create a sorted version of the heights list
        expected = sorted(heights)        
        # count the number of mismatches
        answer = 0
        
        for i in range(len(heights)):
            # If there is a mismatch between the original and sorted lists at index i
            if heights[i] != expected[i]:
                # Increment the mismatch counter
                answer += 1

        return answer