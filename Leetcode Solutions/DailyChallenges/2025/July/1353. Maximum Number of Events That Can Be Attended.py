# problem link: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/


# Description:
"""
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.

 

Example 1:


Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
"""

# Solution:
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        day = 0
        i = 0
        res = 0
        n = len(events)

        # Determine the last possible day
        max_day = max(end for _, end in events)

        for day in range(1, max_day + 1):
            # Add all events starting today
            while i < n and events[i][0] == day:
                heappush(heap, events[i][1])
                i += 1

            # Remove events that have already ended
            while heap and heap[0] < day:
                heappop(heap)

            # Attend the event that ends earliest
            if heap:
                heappop(heap)
                res += 1

        return res