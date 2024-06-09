# problem link: https://leetcode.com/problems/non-overlapping-intervals


# My SOLUTION:

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

	    if not intervals:
	        return 0

	    # Sort the intervals based on the end points
	    intervals.sort(key=lambda x: x[1])

	    non_overlapping_count = 1
	    prev_end = intervals[0][1]

	    # Iterate through the sorted intervals to find non-overlapping intervals
	    for i in range(1, len(intervals)):
	        current_start, current_end = intervals[i]
	        # If the current interval's start point is greater than or equal to prev_end,
	        # there is no overlap so we increment the non_overlapping_count.
	        if current_start >= prev_end:
	            non_overlapping_count += 1
	            prev_end = current_end

	    # The minimum number of intervals to remove is the total number of intervals
	    # minus the non-overlapping count.
	    return len(intervals) - non_overlapping_count