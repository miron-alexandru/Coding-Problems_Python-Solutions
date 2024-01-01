# Problem link:https://leetcode.com/problems/asteroid-collision/

#My Solution:
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:  # Asteroid moving left, stack top moving right
                if abs(asteroid) > stack[-1]:  # Current asteroid destroys the top of the stack
                    stack.pop()
                elif abs(asteroid) == stack[-1]:  # Both asteroids destroy each other
                    stack.pop()
                    break
                else:  # Top of stack destroys the current asteroid
                    break
            else:
                stack.append(asteroid)  # No collision, add the asteroid to the stack

        return stack
