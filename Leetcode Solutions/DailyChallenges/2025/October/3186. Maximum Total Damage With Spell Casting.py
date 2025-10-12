# problem link: https://leetcode.com/problems/maximum-total-damage-with-spell-casting/


# Description:
"""
A magician has various spells.

You are given an array power, where each element represents the damage of a spell. Multiple spells can have the same damage value.

It is a known fact that if a magician decides to cast a spell with a damage of power[i], they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.

Each spell can be cast only once.

Return the maximum possible total damage that a magician can cast.

 

Example 1:

Input: power = [1,1,3,4]

Output: 6

Explanation:

The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.

Example 2:

Input: power = [7,1,6,6]

Output: 13

Explanation:

The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.
"""

# Solution:
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        @cache
        def calculate_max_damage(index: int) -> int:
            if index >= array_length:
                return 0
            skip_current = calculate_max_damage(index + power_count[sorted_power[index]])
            current_damage = sorted_power[index] * power_count[sorted_power[index]]
            take_current = current_damage + calculate_max_damage(next_valid_index[index])
            return max(skip_current, take_current)

        array_length = len(power)
        power_count = Counter(power)
        sorted_power = sorted(power)
        next_valid_index = [
            bisect_right(sorted_power, value + 2, lo=i + 1)
            for i, value in enumerate(sorted_power)
        ]
        return calculate_max_damage(0)