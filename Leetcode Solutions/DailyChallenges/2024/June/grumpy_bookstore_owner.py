# problem link: https://leetcode.com/problems/grumpy-bookstore-owner/


# my solution:

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
    
        # Calculate the initial satisfaction
        initial_satisfaction = sum(customers[i] for i in range(n) if not grumpy[i])
        
        # Calculate the initial gain if the technique is used in the first window of minutes
        current_gain = sum(customers[i] for i in range(minutes) if grumpy[i])
        max_gain = current_gain
        
        # Slide the window from minute minutes to the end of the list
        for i in range(minutes, n):
            # Add the customers of the current minute to current_gain if the owner is grumpy
            if grumpy[i]:
                current_gain += customers[i]
            # Subtract the customers from minutes ago from current_gain if the owner was grumpy
            if grumpy[i - minutes]:
                current_gain -= customers[i - minutes]
            # Update max_gain with the maximum value between max_gain and current_gain
            max_gain = max(max_gain, current_gain)

        return initial_satisfaction + max_gain
