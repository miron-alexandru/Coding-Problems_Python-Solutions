# problem link: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/



# my solution:
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Sort the arrays
        seats.sort()
        students.sort()

        moves = 0
        
        # Iterate through the arrays simultaneously
        for seat, student in zip(seats, students):
            # Calculate the absolute difference between the seat position and the student position
            moves += abs(seat - student)

        return moves

