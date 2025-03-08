# problem link: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/



# solution:
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        current_w = sum(1 for i in range(k) if blocks[i] == 'W')
        min_changes = current_w

        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                current_w -= 1  # Remove leftmost character
            
            if blocks[i] == 'W':
                current_w += 1  # Add new character
            
            min_changes = min(min_changes, current_w)

        return min_changes
