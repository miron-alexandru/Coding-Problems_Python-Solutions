# problem link: https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/


# Description:
"""
You are given two integer arrays, skill and mana, of length n and m, respectively.

In a laboratory, n wizards must brew m potions in order. Each potion has a mana capacity mana[j] and must pass through all the wizards sequentially to be brewed properly. The time taken by the ith wizard on the jth potion is timeij = skill[i] * mana[j].

Since the brewing process is delicate, a potion must be passed to the next wizard immediately after the current wizard completes their work. This means the timing must be synchronized so that each wizard begins working on a potion exactly when it arrives. ​

Return the minimum amount of time required for the potions to be brewed properly.
"""


# Solution:
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        f = [0] * n  # track when each wizard is free

        for x in mana:  # process each potion in order
            now = f[0]  # potion starts at first wizard
            for i in range(1, n):
                # potion reaches next wizard only when both are ready
                now = max(now + skill[i-1] * x, f[i])
            # finish time on last wizard
            f[n-1] = now + skill[n-1] * x
            # adjust previous finish times to stay synchronized
            for i in range(n-2, -1, -1):
                f[i] = f[i+1] - skill[i+1] * x

        return f[-1]  # total time after last potion
