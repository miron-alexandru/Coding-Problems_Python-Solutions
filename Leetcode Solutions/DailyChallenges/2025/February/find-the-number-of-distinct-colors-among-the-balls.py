# problem link: https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls



# solution:
from collections import defaultdict

class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        ball_colors = {}
        color_count = defaultdict(int)
        distinct_colors = set()
        result = []

        for x, y in queries:
            # Check if the ball already has a color
            if x in ball_colors:
                old_color = ball_colors[x]
                # If the ball color is different update it
                if old_color != y:
                    # Decrease count of the old color
                    color_count[old_color] -= 1
                    if color_count[old_color] == 0:
                        distinct_colors.discard(old_color)

                    # Update the ball's color
                    ball_colors[x] = y
                    color_count[y] += 1
                    distinct_colors.add(y)
            else:
                # First time coloring this ball
                ball_colors[x] = y
                color_count[y] += 1
                distinct_colors.add(y)
            
            result.append(len(distinct_colors))

        return result
