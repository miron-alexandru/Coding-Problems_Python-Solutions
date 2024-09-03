# problem link: https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/


# my solution:
class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        total_chalk = sum(chalk)
        
        # Determine remaining chalk after full rounds
        remaining_chalk = k % total_chalk
        
        # Find the student who will need to replace the chalk
        for i, usage in enumerate(chalk):
            if remaining_chalk < usage:
                return i
            remaining_chalk -= usage
        
        return -1