# problem link: https://leetcode.com/problems/my-calendar-i/



# my solution:
class MyCalendar:

    def __init__(self):
        # Store the list of events as tuples (start, end)
        self.events = []
        
    def book(self, start: int, end: int) -> bool:
        # Check if the new event overlaps with any of the existing events
        for event in self.events:
            # If there is any overlap return False
            if max(event[0], start) < min(event[1], end):
                return False
        
        # If no overlap add the event and return True
        self.events.append((start, end))
        return True