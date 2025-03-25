# problem link: https://leetcode.com/problems/count-days-without-meetings/




# solution:
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available_days = 0
        last_meeting_day = 0
        
        for start_day, end_day in meetings:
            if last_meeting_day < start_day:
                available_days += start_day - last_meeting_day - 1
            last_meeting_day = max(last_meeting_day, end_day)
        
        available_days += days - last_meeting_day
        return available_days
