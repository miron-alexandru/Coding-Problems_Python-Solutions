# problem link: https://leetcode.com/problems/minimum-time-difference/



# my solution:


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert time to minutes
        def convertToMinutes(time: str) -> int:
            hours, minutes = map(int, time.split(":"))
            return hours * 60 + minutes
        
        # Convert all times to minutes and sort the minutes list
        minutes_list = [convertToMinutes(time) for time in timePoints]
        minutes_list.sort()
        
        # Find the minimum difference between consecutive times
        min_diff = float('inf')
        for i in range(1, len(minutes_list)):
            min_diff = min(min_diff, minutes_list[i] - minutes_list[i - 1])
        
        # Check the difference between the first and last time points in a circular manner
        circular_diff = (24 * 60 - minutes_list[-1] + minutes_list[0])
        min_diff = min(min_diff, circular_diff)
        
        return min_diff
