# problem link: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence

# my solution:
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        # any array of length 0 or 1 is trivially an arithmetic progression, and any array of length 2 is also an arithmetic progression.
        if len(arr) < 3:
            return True
        # compute common diff
        common_diff = arr[1] - arr[0]

        for i in range(1, len(arr) - 1):
            if arr[i + 1] - arr[i] != common_diff:
                return False

        return True