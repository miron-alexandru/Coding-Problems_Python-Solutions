# problem link: https://leetcode.com/problems/two-best-non-overlapping-events/


# my solution:
from bisect import bisect_right

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        m = len(events)
        max_vals = [events[-1][2]] * m
        
        for i in range(m - 2, -1, -1):
            max_vals[i] = max(max_vals[i + 1], events[i][2])
        
        result = 0
        
        for _, e, v in events:
            idx = bisect_right(events, e, key=lambda x: x[0])
            if idx < m:
                res = v + max_vals[idx]
            else:
                res = v
            result = max(result, res)
        
        return result
