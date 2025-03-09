# problem link: https://leetcode.com/problems/alternating-groups-ii


# solution:
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        alternating_count = max_groups = 0

        for i in range(n * 2):
            if i > 0 and colors[i % n] == colors[(i - 1) % n]:
                alternating_count = 1  # Reset count if two consecutive tiles have the same color
            else:
                alternating_count += 1  # Increase count for alternating tiles
            
            if i >= n and alternating_count >= k:
                max_groups += 1  # Count valid alternating groups

        return max_groups
