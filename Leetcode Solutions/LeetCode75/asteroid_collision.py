# problem link: https://leetcode.com/problems/asteroid-collision


# my solution:
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # If the stack is empty, the asteroid will not collide with anything
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:
                # Handle collisions
                while stack and stack[-1] > 0:
                    top = stack.pop()
                    collision = top + asteroid
                    if collision == 0:
                        # Both asteroids explode
                        break
                    elif collision < 0:
                        # The top asteroid explodes
                        continue
                    else:
                        # The current asteroid explodes
                        stack.append(top)
                        break
                else:
                    # the current asteroid survives
                    stack.append(asteroid)

        return stack




